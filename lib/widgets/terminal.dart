import 'dart:io';

import 'package:flutter/material.dart';
import 'package:pty/pty.dart';
import 'package:xterm/flutter.dart';
import 'package:xterm/xterm.dart';

class LocalTerminalBackend extends TerminalBackend {
  LocalTerminalBackend(PseudoTerminal this.pty);

  final pty;
  @override
  Future<int> get exitCode => pty.exitCode;

  @override
  void init() {
    pty.init();
  }

  @override
  Stream<String> get out {
    // TODO: implement out
    throw UnimplementedError();
  }

  @override
  void resize(int width, int height, int pixelWidth, int pixelHeight) {
    pty.resize(width, height);
  }

  @override
  void write(String input) {
    pty.write(input);
  }

  @override
  void terminate() {
    // client.disconnect('terminate');
  }

  @override
  void ackProcessed() {
    // NOOP
  }
}

class LocalTerminal extends StatefulWidget {
  const LocalTerminal(
    PseudoTerminal this.pty, {
    Key? key,
  }) : super(key: key);
  final PseudoTerminal pty;
  @override
  _LocalTerminalState createState() => _LocalTerminalState();
}

class _LocalTerminalState extends State<LocalTerminal> {
  // final terminal = Terminal(maxLines: 10000, backend: LocalTerminalBackend());

  @override
  void initState() {
    super.initState();
  }

  void onInput(String input) {
    print('input: $input');
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: TerminalView(
          terminal: Terminal(
            maxLines: 10000,
            backend: LocalTerminalBackend(widget.pty),
          ),
        ),
      ),
    );
  }
}
