import 'dart:html';

import 'package:flutter/material.dart';
import 'package:http/http.dart';
import 'package:preco_ai/json_response.dart';
import 'dart:convert';

class HomePage extends StatefulWidget {
  HomePage({Key key, this.title}) : super(key: key);

  final String title;

  @override
  State<HomePage> createState() {
    return HomePageState();
  }
}

class HomePageState extends State<HomePage> {
  var data;
  final searchController = TextEditingController();

  @override
  void dispose() {
    searchController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
          child: ListView(
        shrinkWrap: true,
        children: [
          TextField(
            decoration: InputDecoration(
                border: OutlineInputBorder(), hintText: 'Cidade, Estado'),
            controller: searchController,
          ),
          ElevatedButton(
              child: Text("Buscar"),
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                      builder: (context) => ResultPage(
                            place: searchController.text,
                          )),
                );
              })
        ],
      )),
    );
  }
}

class ResultPage extends StatelessWidget {
  final String place;

  ResultPage({Key key, @required this.place}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(title: Text("Previsão do Tempo")),
        body: Container(
          child: FutureBuilder(
            future: getWeather(place),
            builder: (context, snapshot) {
              if (snapshot.connectionState == ConnectionState.done) {
                ResponseJson data = snapshot.data;
                return ListView(
                  shrinkWrap: true,
                  children: <Widget>[
                    ListTile(
                      leading: Icon(Icons.wine_bar),
                      title: Text(
                        "Clima",
                        style: TextStyle(fontWeight: FontWeight.bold),
                      ),
                      tileColor: Colors.amber,
                      subtitle: Text(
                        data.weather[0].description,
                        style: TextStyle(
                            fontWeight: FontWeight.bold,
                            fontStyle: FontStyle.italic),
                      ),
                    ),
                    ListTile(
                      leading: Icon(Icons.thermostat),
                      title: Text(
                        "Temperatura",
                        style: TextStyle(fontWeight: FontWeight.bold),
                      ),
                      tileColor: Colors.orange,
                      subtitle: Text(
                        data.main.temp.toString() + " ºC",
                        style: TextStyle(
                            fontWeight: FontWeight.bold,
                            fontStyle: FontStyle.italic),
                      ),
                    ),
                    ListTile(
                      leading: Icon(Icons.wb_sunny),
                      title: Text(
                        "Sensação Térmica",
                        style: TextStyle(fontWeight: FontWeight.bold),
                      ),
                      tileColor: Colors.amber,
                      subtitle: Text(
                        data.main.feelsLike.toString() + " ºC",
                        style: TextStyle(
                            fontWeight: FontWeight.bold,
                            fontStyle: FontStyle.italic),
                      ),
                    ),
                    ListTile(
                      leading: Icon(Icons.ac_unit),
                      title: Text(
                        "Temperatura mínima",
                        style: TextStyle(fontWeight: FontWeight.bold),
                      ),
                      tileColor: Colors.orange,
                      subtitle: Text(
                        data.main.tempMin.toString() + " ºC",
                        style: TextStyle(
                            fontWeight: FontWeight.bold,
                            fontStyle: FontStyle.italic),
                      ),
                    ),
                    ListTile(
                      leading: Icon(Icons.cloud),
                      title: Text(
                        "Temperatura máxima",
                        style: TextStyle(fontWeight: FontWeight.bold),
                      ),
                      tileColor: Colors.amber,
                      subtitle: Text(
                        data.main.tempMax.toString() + " ºC",
                        style: TextStyle(
                            fontWeight: FontWeight.bold,
                            fontStyle: FontStyle.italic),
                      ),
                    ),
                    ListTile(
                      leading: Icon(Icons.line_weight),
                      title: Text(
                        "Pressão",
                        style: TextStyle(fontWeight: FontWeight.bold),
                      ),
                      tileColor: Colors.orange,
                      subtitle: Text(
                        data.main.pressure.toString() + " hPa (hectopascal)",
                        style: TextStyle(
                            fontWeight: FontWeight.bold,
                            fontStyle: FontStyle.italic),
                      ),
                    ),
                    ListTile(
                      leading: Icon(Icons.water),
                      title: Text(
                        "Pressão atmosférica no nível do mar",
                        style: TextStyle(fontWeight: FontWeight.bold),
                      ),
                      tileColor: Colors.amber,
                      subtitle: Text(
                        data.main.seaLevel.toString() + " hPa (hectopascal)",
                        style: TextStyle(
                            fontWeight: FontWeight.bold,
                            fontStyle: FontStyle.italic),
                      ),
                    ),
                    ListTile(
                      leading: Icon(Icons.beach_access),
                      title: Text(
                        "Pressão atmosférica no nível do solo",
                        style: TextStyle(fontWeight: FontWeight.bold),
                      ),
                      tileColor: Colors.orange,
                      subtitle: Text(
                        data.main.grndLevel.toString() + " hPa (hectopascal)",
                        style: TextStyle(
                            fontWeight: FontWeight.bold,
                            fontStyle: FontStyle.italic),
                      ),
                    ),
                    ListTile(
                      leading: Icon(Icons.shower),
                      title: Text(
                        "Umidade",
                        style: TextStyle(fontWeight: FontWeight.bold),
                      ),
                      tileColor: Colors.amber,
                      subtitle: Text(
                        data.main.humidity.toString() + "%",
                        style: TextStyle(
                            fontWeight: FontWeight.bold,
                            fontStyle: FontStyle.italic),
                      ),
                    ),
                    ListTile(
                      leading: Icon(Icons.window),
                      title: Text(
                        "Visibilidade",
                        style: TextStyle(fontWeight: FontWeight.bold),
                      ),
                      tileColor: Colors.orange,
                      subtitle: Text(
                        (data.visibility / 1000).toString() + " Km",
                        style: TextStyle(
                            fontWeight: FontWeight.bold,
                            fontStyle: FontStyle.italic),
                      ),
                    ),
                    ListTile(
                      leading: Icon(Icons.speed),
                      title: Text(
                        "Velocidade do vento",
                        style: TextStyle(fontWeight: FontWeight.bold),
                      ),
                      tileColor: Colors.amber,
                      subtitle: Text(
                        data.wind.speed.toString() +
                            " metros/segundo\n" +
                            (data.wind.speed * 3.6).toString() +
                            " km/hora",
                        style: TextStyle(
                            fontWeight: FontWeight.bold,
                            fontStyle: FontStyle.italic),
                      ),
                    ),
                  ],
                );
              } else {
                return Center(
                  child: CircularProgressIndicator(),
                );
              }
            },
          ),
        ));
  }

  Future getWeather(String place) async {
    String token = "3e0e4dc0013f3fd7fe63259a6f4c4529";
    String authority =
        "http://api.openweathermap.org/data/2.5/weather?q=$place&units=metric&lang=pt_br&appid=$token";
    final url = Uri.parse(authority);

    Response response = await get(url);

    Map<String, dynamic> map =
        jsonDecode(response.body) as Map<String, dynamic>;
    ResponseJson returnedData = ResponseJson.fromJson(map);

    return returnedData;
  }

  dynamic makeGet(String place) {
    return FutureBuilder(
      future: getWeather(place),
      builder: (context, snapshot) {
        if (snapshot.connectionState == ConnectionState.done) {
          ResponseJson test = snapshot.data;
          print(test.main.temp);
          return snapshot.data;
        } else {
          return CircularProgressIndicator();
        }
      },
    );
  }
}
