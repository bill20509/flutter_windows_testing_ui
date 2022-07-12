import 'dart:ffi';

import 'package:example/models/test_case.dart';
import 'package:flutter/material.dart';

class itemCard extends StatefulWidget {
  const itemCard({
    Key? key,
    required this.parentSetState,
    required this.q1,
    required this.q2,
    required this.index,
  }) : super(key: key);
  final Function parentSetState;
  final List<TestCase> q1;
  final List<TestCase> q2;
  final int index;
  @override
  State<itemCard> createState() => _itemCardState();
}

class _itemCardState extends State<itemCard> {
  bool display = false;
  bool isChecked = true;
  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(10.0),
      child: Card(
        margin: const EdgeInsets.only(left: 10.0, right: 10.0),
        child: Column(
          children: [
            Container(
              decoration: BoxDecoration(
                color: Colors.black26,
              ),
              child: Row(
                children: [
                  Expanded(
                    child: Tooltip(
                      message: widget.q1[widget.index].name,
                      child: TextButton(
                        style: TextButton.styleFrom(
                          textStyle: const TextStyle(fontSize: 20),
                          minimumSize: const Size.fromHeight(50),
                          primary: Colors.white,
                        ),
                        onPressed: () {
                          widget.parentSetState(() {
                            display = false;
                            TestCase temp = TestCase(
                              widget.q1[widget.index].name,
                              widget.q1[widget.index].path,
                              widget.q1[widget.index].cases,
                            );
                            widget.q1.removeAt(widget.index);
                            widget.q2.add(temp);
                          });
                        },
                        child: Text(
                          widget.q1[widget.index].name,
                          overflow: TextOverflow.ellipsis,
                        ),
                      ),
                    ),
                  ),
                  Checkbox(
                    checkColor: Colors.white,
                    value: isChecked,
                    onChanged: (bool? value) {
                      setState(() {
                        for (var i = 0;
                            i < widget.q1[widget.index].cases.length;
                            i++) {
                          widget.q1[widget.index].cases[i]['isChecked'] = value;
                        }

                        isChecked = value!;
                      });
                    },
                  ),
                  IconButton(
                    onPressed: () {
                      setState(() {
                        display = !display;
                      });
                    },
                    icon: Icon(Icons.arrow_drop_down),
                  )
                ],
              ),
            ),
            display
                ? Column(
                    children: widget.q1[widget.index].cases.map((item) {
                      return CheckboxListTile(
                        value: item["isChecked"],
                        title: Text(item["name"]),
                        onChanged: (newValue) {
                          widget.parentSetState(() {
                            item["isChecked"] = newValue;
                          });
                        },
                      );
                    }).toList(),
                  )
                : Container(),
          ],
        ),
      ),
    );
  }
}
