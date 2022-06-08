import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';
import 'dart:async';
import 'package:pty/pty.dart';
import 'models/test_case.dart';
import 'package:xterm/xterm.dart';
import 'widgets/terminal.dart';
import 'dart:convert';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  MyApp({Key? key}) : super(key: key);
  // This widget is the root of your application.

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        // This is the theme of your application.
        //
        // Try running your application with "flutter run". You'll see the
        // application has a blue toolbar. Then, without quitting the app, try
        // changing the primarySwatch below to Colors.green and then invoke
        // "hot reload" (press "r" in the console where you ran "flutter run",
        // or simply save your changes to "hot reload" in a Flutter IDE).
        // Notice that the counter didn't reset back to zero; the application
        // is not restarted.
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key, required this.title}) : super(key: key);

  // This widget is the home page of your application. It is stateful, meaning
  // that it has a State object (defined below) that contains fields that affect
  // how it looks.

  // This class is the configuration for the state. It holds the values (in this
  // case the title) provided by the parent (in this case the App widget) and
  // used by the build method of the State. Fields in a Widget subclass are
  // always marked "final".

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  List<TestCase> queue1 = [];
  List<TestCase> queue2 = [];
  final pty = PseudoTerminal.start(
    r'C:\windows\system32\WindowsPowerShell\v1.0\powershell.exe',
    [''],
    environment: {'TERM': 'xterm-256color'},
  );

  // Future<List<ProcessResult>> getResult() async {
  //   var shell = Shell();
  //   var result = shell.run("""
  //     pytest ./tests/YCP/fake_test.py
  //   """);
  //   return result;
  // }
  void _runTest() {
    setState(() {
      String test_command = "";
      for (var i in queue2) {
        test_command = test_command + i.name + " ";
      }
      pty.write("echo run ${test_command}\r");
    });
  }

  @override
  void initState() {
    String contents = new File('./ycp_cases.json').readAsStringSync();
    List<dynamic> test_cases = jsonDecode(contents);
    print(test_cases);
    for (var i in test_cases) {
      // print(i["case_name"]);
      List<Map> temp_list_map = [];
      for (var j in i["cases"]) {
        temp_list_map.add({
          "name": j,
          "isChecked": true,
        });
      }
      TestCase temp = TestCase(i["case_name"], i["path"], temp_list_map);
      queue1.add(temp);
    }
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    // This method is rerun every time setState is called, for instance as done
    // by the _incrementCounter method above.
    //
    // The Flutter framework has been optimized to make rerunning build methods
    // fast, so that you can just rebuild anything that needs updating rather
    // than having to individually change instances of widgets.
    // var r = getResult();
    return Scaffold(
      appBar: AppBar(
        // Here we take the value from the MyHomePage object that was created by
        // the App.build method, and use it to set our appbar title.
        title: Text(widget.title),
      ),
      body: Center(
        child: Center(
          child: Body(
            queue1,
            queue2,
            pty,
          ),
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _runTest,
        tooltip: 'Run Tests',
        child: const Icon(Icons.arrow_right_rounded),
      ), // This trailing comma makes auto-formatting nicer for build methods.
    );
  }
}

class Body extends StatefulWidget {
  const Body(
    List<TestCase> this.q1,
    List<TestCase> this.q2,
    PseudoTerminal this.pty, {
    Key? key,
  }) : super(key: key);
  final List<TestCase> q1;
  final List<TestCase> q2;
  final PseudoTerminal pty;
  @override
  State<Body> createState() => _BodyState();
}

class _BodyState extends State<Body> {
  final ScrollController _firstController = ScrollController();
  final ScrollController _secondController = ScrollController();
  // final ScrollController _thirdController = ScrollController();

  List<Map> availableHobbies = [
    {"name": "Foobball", "isChecked": false},
    {"name": "Baseball", "isChecked": false},
    {"name": "Video Games", "isChecked": false},
    {"name": "Readding Books", "isChecked": false},
    {"name": "Surfling The Internet", "isChecked": false}
  ];

  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(
        builder: (BuildContext context, BoxConstraints constraints) {
      return Row(
        children: <Widget>[
          SizedBox(
            width: constraints.maxWidth / 5,
            child: Scrollbar(
              controller: _firstController,
              isAlwaysShown: true,
              child: ListView.builder(
                  controller: _firstController,
                  itemCount: widget.q1.length,
                  itemBuilder: (BuildContext context, int index) {
                    return Padding(
                      padding: const EdgeInsets.all(10.0),
                      child: Container(
                        child: Column(
                          children: [
                            TextButton(
                              style: TextButton.styleFrom(
                                textStyle: const TextStyle(fontSize: 20),
                                minimumSize: const Size.fromHeight(50),
                                backgroundColor:
                                    Color.fromARGB(118, 210, 169, 169),
                              ),
                              onPressed: () {
                                setState(() {
                                  TestCase temp = TestCase(
                                    widget.q1[index].name,
                                    widget.q1[index].path,
                                    widget.q1[index].cases,
                                  );
                                  widget.q1.removeAt(index);
                                  widget.q2.add(temp);
                                });
                              },
                              child: Text(widget.q1[index].name),
                            ),
                            Column(
                                children: widget.q1[index].cases.map((item) {
                              return CheckboxListTile(
                                  value: item["isChecked"],
                                  title: Text(item["name"]),
                                  onChanged: (newValue) {
                                    setState(() {
                                      item["isChecked"] = newValue;
                                    });
                                  });
                            }).toList()),
                          ],
                        ),
                      ),
                    );
                  }),
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
            width: constraints.maxWidth / 5,
            child: Scrollbar(
              controller: _secondController,
              isAlwaysShown: true,
              child: ListView.builder(
                  controller: _secondController,
                  itemCount: widget.q2.length,
                  itemBuilder: (BuildContext context, int index) {
                    return Padding(
                      padding: const EdgeInsets.all(2.0),
                      child: TextButton(
                        style: TextButton.styleFrom(
                          textStyle: const TextStyle(fontSize: 20),
                          backgroundColor: Color.fromARGB(118, 210, 169, 169),
                        ),
                        onPressed: () {
                          setState(() {
                            TestCase temp = TestCase(
                              widget.q2[index].name,
                              widget.q2[index].path,
                              widget.q2[index].cases,
                            );
                            widget.q2.removeAt(index);
                            widget.q1.add(temp);
                          });
                        },
                        child: Text(widget.q2[index].name),
                      ),
                    );
                  }),
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
            child: LocalTerminal(widget.pty),
          ),
        ],
      );
    });
  }
}
