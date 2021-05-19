import 'package:flutter/material.dart';
import 'package:preco_ai/homepage.dart';

class AppWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Preço Aí',
      theme: ThemeData(
        primarySwatch: Colors.red,
        backgroundColor: Colors.black,
      ),
      home: HomePage(title: 'Consulta o Preço Aí'),
    );
  }
}