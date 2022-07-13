import 'dart:ffi';
import 'dart:io';

import 'package:example/widgets/item_card.dart';
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
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: 'Demo Page'),
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

class _MyHomePageState extends State<MyHomePage> {
  List<TestCase> queue1 = [];
  List<TestCase> queue2 = [];
  int mode = 0; // 0 -> YCP, 1 -> YMK
  final pty = PseudoTerminal.start(
    r'C:\windows\system32\WindowsPowerShell\v1.0\powershell.exe',
    [''],
    environment: {'TERM': 'xterm-256color'},
  );

  void _runTest() {
    if (queue2.isEmpty) return;
    setState(() {
      String test_command = "python3 maintest.py ";
      for (var i in queue2) {
        for (var j in i.cases) {
          if (j["isChecked"]) {
            test_command = test_command + i.path + "::Test::" + j["name"] + " ";
          }
        }
      }
      pty.write("${test_command} \r");
    });
  }

  void _parse() {
    pty.write("python3 parse.py\r");
  }

  void _loadTestCase() {
    queue1 = [];
    queue2 = [];
    String contents = "";
    if (mode == 0) {
      contents = new File('./YCP_cases.json').readAsStringSync();
    } else if (mode == 1) {
      contents = new File('./YMK_cases.json').readAsStringSync();
    }
    List<dynamic> test_cases = jsonDecode(contents);
    // print(test_cases);
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
  }

  @override
  void initState() {
    _parse();
    _loadTestCase();
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
        actions: [
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
                  _loadTestCase();
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
                  _loadTestCase();
                });
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
                });
              },
            ),
          ),
          Container(
            decoration: BoxDecoration(
              color: Color.fromARGB(255, 105, 99, 99),
            ),
            padding: const EdgeInsets.all(8.0),
            child: IconButton(
              icon: const Icon(Icons.save),
              tooltip: 'Save',
              onPressed: () {
                setState(() {
                  _loadTestCase();
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
  List<Bool> displayCheckList = [];
  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(
        builder: (BuildContext context, BoxConstraints constraints) {
      return Row(
        children: <Widget>[
          Column(
            children: [
              SizedBox(
                width: constraints.maxWidth / 5,
                height: constraints.maxHeight * 0.95,
                child: Scrollbar(
                  controller: _firstController,
                  isAlwaysShown: true,
                  child: ListView.builder(
                      controller: _firstController,
                      itemCount: widget.q1.length,
                      itemBuilder: (BuildContext context, int index) {
                        return itemCard(
                          parentSetState: setState,
                          q1: widget.q1,
                          q2: widget.q2,
                          index: index,
                        );
                      }),
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
            child: Scrollbar(
              controller: _secondController,
              isAlwaysShown: true,
              child: ListView.builder(
                  controller: _secondController,
                  itemCount: widget.q2.length,
                  itemBuilder: (BuildContext context, int index) {
                    return itemCard(
                      parentSetState: setState,
                      q1: widget.q2,
                      q2: widget.q1,
                      index: index,
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
