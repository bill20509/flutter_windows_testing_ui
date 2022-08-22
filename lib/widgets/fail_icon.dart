import 'dart:async';
import 'dart:io';

import 'package:example/models/test_case.dart';
import 'package:flutter/material.dart';
import 'package:badges/badges.dart';
import 'package:flutter_json_viewer/flutter_json_viewer.dart';
import 'dart:convert';

class FailIcon extends StatefulWidget {
  const FailIcon({
    Key? key,
    required this.tempJsonFileName,
  }) : super(key: key);
  final String tempJsonFileName;
  @override
  State<FailIcon> createState() => _FailIconState();
}

class _FailIconState extends State<FailIcon> {
  Timer? timer;
  int failCount = 0;
  @override
  void initState() {
    timer =
        Timer.periodic(Duration(seconds: 5), (Timer t) => refreshFailCount());
    super.initState();
  }

  void refreshFailCount() {
    print(failCount);
    final contents = File(widget.tempJsonFileName).readAsLinesSync();

    List<Map<String, dynamic>> failCases = [];
    for (final item in contents) {
      Map<String, dynamic> testCase = jsonDecode(item);
      if (testCase['outcome'] == 'failed') {
        failCases.add(testCase);
      }
    }
    setState(() {
      failCount = failCases.length;
    });
  }

  @override
  void dispose() {
    timer?.cancel();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        color: failCount == 0 ? Colors.green : Colors.red,
      ),
      margin: EdgeInsets.zero,
      child: Badge(
        badgeColor: Colors.white,
        badgeContent: Text('$failCount'),
        child: failCount == 0 ? Icon(Icons.check) : Icon(Icons.warning),
      ),
    );
  }
}
