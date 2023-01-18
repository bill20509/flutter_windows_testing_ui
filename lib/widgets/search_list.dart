import 'dart:async';
import 'dart:convert';
import 'dart:io';

import 'package:flutter/material.dart';

class SearchList extends StatefulWidget {
  const SearchList({Key? key}) : super(key: key);

  @override
  State<SearchList> createState() => _SearchListState();
}

class _SearchListState extends State<SearchList> {
  List<String> content = ['no tests'];
  List<String> resultList = [];
  int count = 0;
  late Timer _everySecond;

  @override
  void initState() {
    super.initState();
    _everySecond = Timer.periodic(Duration(seconds: 1), (Timer t) {
      try {
        var f = File("search.temp");
        var contents = f.readAsStringSync();
        // var utf16CodeUnits = bytes.buffer.asUint16List();
        // print(contents);
        // var s = String.fromCharCodes(utf16CodeUnits);
        // print(s);
        LineSplitter ls = new LineSplitter();
        List<String> _masForUsing = ls.convert(contents);
        for (var i = 0; i < _masForUsing.length; i++) {
          _masForUsing[i] =
              _masForUsing[i].replaceAll(RegExp(r'[^a-zA-Z0-9_\/:\.]+'), '');
          // print('${i} ${_masForUsing[i]}');
        }
        _masForUsing.sort();

        setState(() {
          content = _masForUsing;
          resultList = [];
          for (var i in content) {
            if (i.startsWith('tests')) {
              count += 1;
              resultList.add(i);
            } else if (i.startsWith('no')) {
              resultList.add('No test founded');
            }
          }
        });
      } on Exception catch (e) {
        print(e);
      }
    });
  }

  @override
  void dispose() {
    super.dispose();
    _everySecond.cancel();
  }

  @override
  Widget build(BuildContext context) {
    return AlertDialog(
      actions: [
        TextButton(
          onPressed: () => Navigator.pop(context, ['']),
          child: Text('Cancel'),
        ),
        TextButton(
          onPressed:
              count == 0 ? null : () => Navigator.pop(context, resultList),
          child: Text('Run test'),
        ),
      ],
      content: SizedBox(
        width: MediaQuery.of(context).size.width * 0.5,
        height: MediaQuery.of(context).size.height * 0.8,
        child: ListView.separated(
          itemBuilder: (context, index) {
            return ListTile(
              title: Text('${index + 1}: ${resultList[index]}'),
            );
          },
          separatorBuilder: (context, index) => const Divider(),
          itemCount: resultList.length,
        ),
      ),
    );
  }
}
