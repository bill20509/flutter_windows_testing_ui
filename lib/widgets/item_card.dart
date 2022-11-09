import 'package:example/models/test_case.dart';
import 'package:flutter/material.dart';

class itemCard extends StatefulWidget {
  const itemCard({
    Key? key,
    required this.parentSetState,
    required this.q1,
    required this.q2,
    required this.index,
    required this.isCheckedList,
  }) : super(key: key);
  final Function parentSetState;
  final List<TestCase> q1;
  final List<TestCase> q2;
  final List<bool> isCheckedList;
  final int index;
  @override
  State<itemCard> createState() => _itemCardState();
}

class _itemCardState extends State<itemCard>
    with AutomaticKeepAliveClientMixin {
  bool display = false;

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
                      child: Text(
                        widget.q1[widget.index].name,
                        overflow: TextOverflow.ellipsis,
                        style: TextStyle(
                          fontSize: 20,
                        ),
                      ),
                    ),
                  ),
                  Checkbox(
                    checkColor: Colors.white,
                    value: widget.isCheckedList[widget.index],
                    onChanged: (bool? value) {
                      widget.parentSetState(() {
                        for (var i = 0;
                            i < widget.q1[widget.index].cases.length;
                            i++) {
                          widget.q1[widget.index].cases[i]['isChecked'] = value;
                        }

                        widget.isCheckedList[widget.index] = value!;
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

  @override
  bool get wantKeepAlive => true;
}
