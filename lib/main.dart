import 'package:example/widgets/fail_icon.dart';
import 'package:example/widgets/search_list.dart';
import 'package:file_picker/file_picker.dart';
import 'package:flutter/foundation.dart';
import 'dart:io';
import 'dart:async';
import 'dart:convert';
import 'package:example/widgets/item_card.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_pty/flutter_pty.dart';
import 'models/test_case.dart';
import 'package:flutter_json_viewer/flutter_json_viewer.dart';
import 'package:xterm/xterm.dart';
import 'package:example/widgets/xterm_mac.dart';
import 'package:path/path.dart' as p;

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  runApp(MyApp());
}

bool get isDesktop {
  if (kIsWeb) return false;
  return [
    TargetPlatform.windows,
    TargetPlatform.linux,
    TargetPlatform.macOS,
  ].contains(defaultTargetPlatform);
}

class MyApp extends StatelessWidget {
  MyApp({Key? key}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: 'UI Testing Tool'),
      debugShowCheckedModeBanner: false,
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key, required this.title}) : super(key: key);
  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

void refreshList(
  List<TestCase> q1,
  List<TestCase> q2,
) {
  q2.clear();
  for (final testCase in q1) {
    final List<Map> cases = [];
    for (final i in testCase.cases) {
      if (i["isChecked"]) {
        cases.add(i);
      }
    }
    TestCase temp = TestCase(
      testCase.name,
      testCase.path,
      cases,
    );
    if (cases.length != 0) {
      q2.add(temp);
    }
  }
}

class _MyHomePageState extends State<MyHomePage> {
  List<TestCase> queue1 = [];
  List<TestCase> queue2 = [];
  List<bool> isCheckedList = [];
  late TextEditingController _controller;
  late TextEditingController _controller2;
  late String pythonName;
  String pwd = "";
  int failCount = 0;
  String tempJsonFileName = 'fail_json.temp';
  int mode = 0; // 0 -> YCP, 1 -> YMK
  late final Pty pty;
  final terminal = Terminal(
    maxLines: 10000,
  );
  bool isAndroid = false;
  void _runTest() {
    if (queue2.isEmpty) return;
    setState(() {
      String test_command = "${pythonName} maintest.py ";
      for (var i in queue2) {
        for (var j in i.cases) {
          if (j["isChecked"]) {
            test_command = test_command + i.path + "::Test::" + j["name"] + " ";
          }
        }
      }
      pty.write(Utf8Encoder().convert("${test_command}\r"));
    });
  }

  void _parse() {
    final platform = isAndroid ? "Android" : "iOS";
    pty.write(Utf8Encoder().convert("${pythonName} parse.py ${platform}\r"));
  }

  void _loadTestCase(bool checked) {
    queue1 = [];
    queue2 = [];
    isCheckedList = [];
    String contents = "";

    try {
      if (mode == 0) {
        contents = File(p.join(pwd, './YCP_cases.json')).readAsStringSync();
      } else if (mode == 1) {
        contents = File(p.join(pwd, './YMK_cases.json')).readAsStringSync();
      }
      List<dynamic> test_cases = jsonDecode(contents);
      for (var i in test_cases) {
        List<Map> temp_list_map = [];
        for (var j in i["cases"]) {
          temp_list_map.add({
            "name": j,
            "isChecked": checked,
          });
        }
        TestCase temp = TestCase(i["case_name"], i["path"], temp_list_map);
        queue1.add(temp);
        isCheckedList.add(true);
      }
    } catch (e) {}
  }

  void _startPty() {
    pty = Pty.start(
      shell,
      columns: terminal.viewWidth,
      rows: terminal.viewHeight,
    );

    pty.output.cast<List<int>>().transform(Utf8Decoder()).listen(
      (event) {
        terminal.write(event);
        if (event.startsWith('/Users/')) {
          pwd = event.trim();
        }
      },
    );

    pty.exitCode.then((code) {
      terminal.write('the process exited with exit code $code');
    });

    terminal.onOutput = (data) {
      pty.write(const Utf8Encoder().convert(data));
    };

    terminal.onResize = (w, h, pw, ph) {
      pty.resize(h, w);
    };
  }

  void _cd() {
    pty.write(const Utf8Encoder().convert(r'echo ${TEST_UI_PATH}' + '\r'));
    pty.write(const Utf8Encoder().convert(r'cd ${TEST_UI_PATH}' + '\r'));
  }

  @override
  void initState() {
    super.initState();
    _startPty();
    _controller = TextEditingController(text: 'python3');
    _controller2 = TextEditingController();
    pythonName = _controller.text;
    _cd();
    _parse();
    _loadTestCase(true);
    refreshList(queue1, queue2);
  }

  void refreshFailCount() {
    setState(() {
      failCount++;
    });
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
        actions: [
          Container(
            decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.all(Radius.circular(5)),
            ),
            width: 150,
            margin: EdgeInsets.symmetric(vertical: 3, horizontal: 3),
            child: TextField(
              decoration: InputDecoration(
                hintText: 'Mark search',
                border: InputBorder.none,
                suffixIcon: IconButton(
                  onPressed: () async {
                    var app_name = mode == 0 ? "YCP" : "YMK";
                    final platform = isAndroid ? "Android" : "iOS";
                    final String command =
                        "${_controller.text} -m pytest ${pwd}/tests/${platform}/${app_name}/ -m \"${_controller2.text}\" --collectonly -q --disable-warnings > search.temp\r";
                    pty.write(Utf8Encoder().convert(command));
                    final result = await showDialog<List<String>>(
                      context: context,
                      builder: (context) {
                        return SearchList();
                      },
                    );
                    if (result != null && result.length > 1) {
                      String test_command = "${pythonName} maintest.py ";
                      for (var i in result) {
                        test_command += "$i ";
                      }
                      pty.write(Utf8Encoder().convert("$test_command\r"));
                    } else {
                      print('cancel');
                    }
                  },
                  icon: Icon(Icons.search),
                  color: Colors.black,
                ),
              ),
              style: TextStyle(color: Colors.grey),
              controller: _controller2,
            ),
          ),
          Container(
            decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.all(Radius.circular(5)),
            ),
            width: 150,
            margin: EdgeInsets.symmetric(vertical: 3, horizontal: 0),
            child: TextField(
              decoration: InputDecoration(
                border: InputBorder.none,
              ),
              style: TextStyle(color: Colors.grey),
              controller: _controller,
              onChanged: (String name) {
                pythonName = name;
              },
            ),
          ),
          Container(
            decoration: BoxDecoration(
              color: Color.fromARGB(255, 72, 68, 72),
              gradient: LinearGradient(
                colors: <Color>[
                  Color.fromARGB(255, 72, 68, 72),
                  Color.fromARGB(255, 30, 4, 22),
                ],
              ),
              borderRadius: BorderRadius.circular(4),
            ),
            padding: const EdgeInsets.all(8.0),
            child: TextButton(
              child: Text(
                'Import Preset',
                overflow: TextOverflow.ellipsis,
              ),
              style: TextButton.styleFrom(
                padding: const EdgeInsets.all(16.0),
                primary: Colors.white,
                textStyle: const TextStyle(fontSize: 15),
              ),
              onPressed: () async {
                FilePickerResult? result = await FilePicker.platform.pickFiles(
                  type: FileType.custom,
                  allowedExtensions: ['json'],
                );
                if (result?.files.single.path != null) {
                  String file =
                      File("${result?.files.single.path}").readAsStringSync();
                  try {
                    Map<String, dynamic> testCases = jsonDecode(file);

                    setState(() {
                      mode = testCases['mode'];
                      _loadTestCase(false);
                      List<dynamic> cases = testCases['testCases'];
                      for (final item in cases) {
                        for (int i = 0; i < queue1.length; i++) {
                          if (queue1[i].name == item['name']) {
                            for (int j = 0;
                                j < (item['cases'] as List).length;
                                j++) {
                              for (int k = 0; k < queue1[i].cases.length; k++) {
                                if (queue1[i].cases[k]['name'] ==
                                    item['cases'][j]['name']) {
                                  queue1[i].cases[k]['isChecked'] = true;
                                }
                              }
                            }
                          }
                        }
                      }
                      refreshList(queue1, queue2);
                    });
                  } catch (e) {
                    print(e);
                  }
                }
              },
            ),
          ),
          Container(
            decoration: BoxDecoration(
              color: Color.fromARGB(255, 6, 222, 63),
              gradient: LinearGradient(
                colors: <Color>[
                  Color.fromARGB(255, 6, 222, 63),
                  Color.fromARGB(255, 181, 216, 5),
                ],
              ),
              borderRadius: BorderRadius.circular(4),
            ),
            padding: const EdgeInsets.all(8.0),
            child: TextButton(
              child: Text(
                'Save Preset',
                overflow: TextOverflow.ellipsis,
              ),
              style: TextButton.styleFrom(
                padding: const EdgeInsets.all(16.0),
                primary: Colors.white,
                textStyle: const TextStyle(fontSize: 15),
              ),
              onPressed: () async {
                String? outputFile = await FilePicker.platform.saveFile(
                  dialogTitle: 'Please select an output file:',
                  fileName: 'preset.json',
                  type: FileType.custom,
                  allowedExtensions: ['json'],
                );
                if (outputFile == null) {
                  return;
                  // User canceled the picker
                }
                setState(
                  () {
                    Map<String, dynamic> saveFile = {
                      'mode': mode,
                      'testCases': []
                    };
                    for (var i = 0; i < queue2.length; i++) {
                      Map<String, dynamic> temp_map = {};
                      temp_map['name'] = queue2[i].name;
                      temp_map['path'] = queue2[i].path;
                      temp_map['class'] = 'Test';
                      var temp_list = [];
                      for (final item in queue2[i].cases) {
                        temp_list.add(item);
                      }
                      temp_map['cases'] = temp_list;
                      saveFile['testCases'].add(temp_map);
                    }
                    var content = jsonEncode(saveFile);

                    var file = File(outputFile);
                    file.writeAsString(jsonEncode(saveFile));
                  },
                );
              },
            ),
          ),
          Container(
            decoration: BoxDecoration(
              color: Colors.purple,
              gradient: LinearGradient(
                colors: <Color>[
                  Color.fromARGB(255, 174, 17, 189),
                  Color.fromARGB(255, 136, 18, 98),
                ],
              ),
              borderRadius: BorderRadius.circular(4),
            ),
            padding: const EdgeInsets.all(8.0),
            child: TextButton(
              child: Text(
                'YouCam Perfect',
                overflow: TextOverflow.ellipsis,
              ),
              style: TextButton.styleFrom(
                padding: const EdgeInsets.all(16.0),
                primary: Colors.white,
                textStyle: const TextStyle(fontSize: 15),
              ),
              onPressed: () {
                setState(() {
                  mode = 0;
                  _loadTestCase(true);
                  refreshList(queue1, queue2);
                });
              },
            ),
          ),
          Container(
            decoration: BoxDecoration(
              gradient: LinearGradient(
                colors: <Color>[
                  Color.fromARGB(255, 204, 54, 110),
                  Color.fromARGB(255, 204, 54, 162),
                ],
              ),
              borderRadius: BorderRadius.circular(4),
            ),
            padding: const EdgeInsets.all(8.0),
            child: TextButton(
              child: Text(
                'YouCam MakeUp',
                overflow: TextOverflow.ellipsis,
              ),
              style: TextButton.styleFrom(
                padding: const EdgeInsets.all(16.0),
                primary: Colors.white,
                textStyle: const TextStyle(fontSize: 15),
              ),
              onPressed: () {
                setState(() {
                  mode = 1;
                  _loadTestCase(true);
                  refreshList(queue1, queue2);
                });
              },
            ),
          ),
          Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Switch(
                // This bool value toggles the switch.r
                value: isAndroid,
                activeColor: Colors.white,
                onChanged: (bool value) {
                  // This is called when the user toggles the switch.
                  setState(() {
                    isAndroid = value;
                    _parse();
                  });
                },
              ),
              if (isAndroid) Text('Android') else Text('iOS'),
            ],
          ),
          Container(
            child: ElevatedButton(
              style: ElevatedButton.styleFrom(
                minimumSize: Size.zero, // Set this
                padding: EdgeInsets.zero, // and this
              ),
              child: FailIcon(tempJsonFileName: p.join(pwd, tempJsonFileName)),
              onPressed: () async {
                final result = await showDialog<String>(
                  context: context,
                  builder: (BuildContext context) {
                    try {
                      final contents =
                          File(p.join(pwd, tempJsonFileName)).readAsLinesSync();

                      List<Map<String, dynamic>> failCases = [];
                      for (final item in contents) {
                        Map<String, dynamic> testCase = jsonDecode(item);
                        if (testCase['outcome'] == 'failed') {
                          failCases.add(testCase);
                        }
                      }
                      return AlertDialog(
                        title: const Text('Failed cases'),
                        content: SizedBox(
                          width: MediaQuery.of(context).size.width * 0.5,
                          height: MediaQuery.of(context).size.height * 0.8,
                          child: ListView.separated(
                            itemBuilder: (context, index) => Card(
                              child: ListTile(
                                  title: Column(
                                    crossAxisAlignment:
                                        CrossAxisAlignment.start,
                                    children: [
                                      Text(
                                        '${index + 1}: ${failCases[index]['location'][0]}',
                                        style: TextStyle(fontSize: 24),
                                      ),
                                      Text(
                                          '${failCases[index]['location'][2]}'),
                                    ],
                                  ),
                                  subtitle: Container(
                                      child: Column(
                                    children: [
                                      JsonViewer({
                                        "code": failCases[index]['longrepr']
                                                ['reprtraceback']['reprentries']
                                            [0]['data']['lines'],
                                      }),
                                      JsonViewer({
                                        "file_name": failCases[index]
                                                    ['longrepr']
                                                ['reprtraceback']['reprentries']
                                            [0]['data']['reprfileloc']['path'],
                                        "line_number": failCases[index]
                                                        ['longrepr']
                                                    ['reprtraceback']
                                                ['reprentries'][0]['data']
                                            ['reprfileloc']['lineno'],
                                        "message": failCases[index]['longrepr']
                                            ['reprcrash']['message']
                                      }),
                                    ],
                                  ))),
                            ),
                            separatorBuilder: (context, index) =>
                                const Divider(),
                            itemCount: failCases.length,
                          ),
                        ),
                        actions: <Widget>[
                          TextButton(
                            onPressed: () => Navigator.pop(context, 'Cancel'),
                            child: const Text('Cancel'),
                          ),
                          TextButton(
                            onPressed: () => Navigator.pop(context, 'OK'),
                            child: const Text('Run these Cases'),
                          ),
                        ],
                      );
                    } catch (e) {
                      return AlertDialog(
                        content: Text('No fail tests'),
                        actions: <Widget>[
                          TextButton(
                            onPressed: () => Navigator.pop(context, 'OK'),
                            child: const Text('OK'),
                          ),
                        ],
                      );
                    }
                  },
                );
                if (result == 'OK') {
                  setState(() {
                    final contents =
                        File(p.join(pwd, tempJsonFileName)).readAsLinesSync();

                    List<Map<String, dynamic>> failCases = [];
                    for (final item in contents) {
                      Map<String, dynamic> testCase = jsonDecode(item);
                      if (testCase['outcome'] == 'failed') {
                        failCases.add(testCase);
                      }
                    }
                    _loadTestCase(false);
                    try {
                      for (final jsonItem in failCases) {
                        final name =
                            ((jsonItem['location'] as List)[0] as String)
                                .split('\\')
                                .last;

                        for (int i = 0; i < queue1.length; i++) {
                          if (queue1[i].name == name) {
                            final caseName =
                                ((jsonItem['location'] as List)[2] as String)
                                    .split('.')
                                    .last;

                            for (int k = 0; k < queue1[i].cases.length; k++) {
                              if (queue1[i].cases[k]['name'] == caseName) {
                                queue1[i].cases[k]['isChecked'] = true;
                              }
                            }
                          }
                        }
                      }
                    } catch (e) {}

                    refreshList(queue1, queue2);
                  });
                }
              },
            ),
          ),
          Container(
            decoration: BoxDecoration(
              color: Colors.grey,
            ),
            padding: const EdgeInsets.all(8.0),
            child: IconButton(
              icon: const Icon(Icons.change_circle),
              tooltip: 'Reload',
              onPressed: () {
                setState(() {
                  _parse();
                  refreshList(queue1, queue2);
                });
              },
            ),
          ),
        ],
      ),
      body: Center(
        child: Center(
          child: Body(
            queue1,
            queue2,
            isCheckedList,
            terminal,
            pty,
          ),
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _runTest,
        tooltip: 'Run Tests',
        child: const Icon(
          Icons.arrow_right_outlined,
          size: 48.0,
        ),
      ), // This trailing comma makes auto-formatting nicer for build methods.
    );
  }
}

class Body extends StatefulWidget {
  const Body(
    List<TestCase> this.q1,
    List<TestCase> this.q2,
    List<bool> this.isCheckedList,
    Terminal this.terminal,
    Pty this.pty, {
    Key? key,
  }) : super(key: key);
  final List<TestCase> q1;
  final List<TestCase> q2;
  final Terminal terminal;
  final Pty pty;
  final List<bool> isCheckedList;
  @override
  State<Body> createState() => _BodyState();
}

class _BodyState extends State<Body> {
  final ScrollController _firstController = ScrollController();
  final ScrollController _secondController = ScrollController();
  bool selectAll = true;

  @override
  void initState() {
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    refreshList(widget.q1, widget.q2);
    return LayoutBuilder(
        builder: (BuildContext context, BoxConstraints constraints) {
      return Row(
        children: <Widget>[
          Column(
            children: [
              Row(
                children: [
                  Builder(
                    builder: (BuildContext ctx) {
                      int count = 0;
                      for (final item in widget.q1) {
                        for (final item2 in item.cases) {
                          count += 1;
                        }
                      }
                      return Text('Total Cases: $count');
                    },
                  ),
                  Checkbox(
                      value: selectAll,
                      onChanged: (value) {
                        setState(() {
                          selectAll = !selectAll;
                          for (int index = 0;
                              index < widget.isCheckedList.length;
                              index++) {
                            widget.isCheckedList[index] = selectAll;
                          }
                          for (int index = 0;
                              index < widget.q1.length;
                              index++) {
                            for (int j = 0;
                                j < widget.q1[index].cases.length;
                                j++) {
                              widget.q1[index].cases[j]['isChecked'] =
                                  selectAll;
                            }
                          }
                        });
                      }),
                ],
              ),
              Expanded(
                child: SizedBox(
                  width: constraints.maxWidth / 5,
                  height: constraints.maxHeight * 0.95,
                  child: Scrollbar(
                    controller: _firstController,
                    child: ListView.builder(
                      controller: _firstController,
                      itemCount: widget.q1.length,
                      itemBuilder: (BuildContext context, int index) {
                        return itemCard(
                          parentSetState: setState,
                          q1: widget.q1,
                          q2: widget.q2,
                          isCheckedList: widget.isCheckedList,
                          index: index,
                        );
                      },
                    ),
                  ),
                ),
              ),
            ],
          ),
          VerticalDivider(
            width: constraints.maxWidth * 0.1 / 5,
            thickness: 1,
            indent: 20,
            endIndent: 0,
            color: Colors.grey,
          ),
          SizedBox(
            width: constraints.maxWidth / 5,
            child: Column(
              children: [
                Builder(builder: (BuildContext ctx) {
                  int count = 0;
                  for (final item in widget.q2) {
                    for (final item2 in item.cases) {
                      count += 1;
                    }
                  }
                  return Text('Running cases: $count');
                }),
                Expanded(
                  child: Scrollbar(
                    controller: _secondController,
                    child: ListView.builder(
                      controller: _secondController,
                      itemCount: widget.q2.length,
                      itemBuilder: (BuildContext context, int index) {
                        return Card(
                          child: ListTile(
                            title: Text(widget.q2[index].name),
                            subtitle: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                for (final run_case in widget.q2[index].cases)
                                  Text('- ${run_case['name']}'),
                              ],
                            ),
                          ),
                        );
                      },
                    ),
                  ),
                ),
              ],
            ),
          ),
          VerticalDivider(
            width: constraints.maxWidth * 0.1 / 5,
            thickness: 1,
            indent: 20,
            endIndent: 0,
            color: Colors.grey,
          ),
          SizedBox(
            width: constraints.maxWidth * 2.8 / 5,
            child: xterm(widget.pty, widget.terminal),
          ),
        ],
      );
    });
  }
}
