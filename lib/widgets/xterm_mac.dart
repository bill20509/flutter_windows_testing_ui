import 'dart:convert';
import 'dart:io';

import './platform_menu.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_acrylic/flutter_acrylic.dart';
import 'package:flutter_pty/flutter_pty.dart';
import 'package:xterm/xterm.dart';

bool get isDesktop {
  if (kIsWeb) return false;
  return [
    TargetPlatform.windows,
    TargetPlatform.linux,
    TargetPlatform.macOS,
  ].contains(defaultTargetPlatform);
}

class xterm extends StatelessWidget {
  xterm(Pty this.pty, Terminal this.terminal);
  final pty;
  final terminal;
  @override
  Widget build(BuildContext context) {
    return AppPlatformMenu(
      child: Home(
        pty: pty,
        terminal: terminal,
      ),
    );
  }
}

class Home extends StatefulWidget {
  Home({required Pty this.pty, required this.terminal, Key? key})
      : super(key: key);
  final Pty pty;
  final Terminal terminal;
  @override
  // ignore: library_private_types_in_public_api
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
  // late final terminal = widget.terminal;

  final terminalController = TerminalController();

  // late final Pty pty = widget.pty;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      body: SafeArea(
        child: TerminalView(
          widget.terminal,
          controller: terminalController,
          autofocus: true,
          backgroundOpacity: 0.7,
          onSecondaryTapDown: (details, offset) async {
            final selection = terminalController.selection;
            if (selection != null) {
              final text = widget.terminal.buffer.getText(selection);
              terminalController.clearSelection();
              await Clipboard.setData(ClipboardData(text: text));
            } else {
              final data = await Clipboard.getData('text/plain');
              final text = data?.text;
              if (text != null) {
                widget.terminal.paste(text);
              }
            }
          },
        ),
      ),
    );
  }
}

String get shell {
  if (Platform.isMacOS || Platform.isLinux) {
    return Platform.environment['SHELL'] ?? 'bash';
  }

  if (Platform.isWindows) {
    return 'cmd.exe';
  }

  return 'sh';
}
