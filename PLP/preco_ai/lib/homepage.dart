import 'package:flutter/material.dart';
import 'package:http/http.dart';
import 'package:preco_ai/json_response.dart';
import 'dart:convert';
import 'package:json_table/json_table.dart';

class HomePage extends StatefulWidget {
  HomePage({Key key, this.title}) : super(key: key);

  final String title;

  @override
  State<HomePage> createState() {
    return HomePageState();
  }
}

class HomePageState extends State<HomePage> {
  int counter = 0;
  String token = "d006e4751057f5dd9c0a174ebc108c292271797a";
  var data;

  void _incrementCounter() {
    setState(() {
      counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    String description = "coca";
    String jsinFucked =
        '[    {        "codGetin": "07894900010015",        "codNcm": "22021000",        "dscProduto": "REFRI COCA COLA LT 350ML",        "valMinimoVendido": 0.01,        "valMaximoVendido": 3.75,        "dthEmissaoUltimaVenda": "2017-10-16T10:03:15.000+0000",        "valUnitarioUltimaVenda": 3.75,        "valUltimaVenda": 0.01,        "numCNPJ": "12268876000364",        "nomRazaoSocial": "RENOVADORA DE PNEUS OK LTDA",        "nomFantasia": null,        "numTelefone": null,        "nomLogradouro": "R   JANGADEIROS ALAGOANOS",        "numImovel": "1351",        "nomBairro": "PAJUSSARA",        "numCep": "57030000",        "nomMunicipio": "MACEIO",        "numLatitude": -9.6639846,        "numLongitude": -35.7111234    },    {        "codGetin": null,        "codNcm": "22021000",        "dscProduto": "REFRI COCA COLA L 350 ML RESTAURANTE",        "valMinimoVendido": 0.01,        "valMaximoVendido": 7.5,        "dthEmissaoUltimaVenda": "2017-10-16T22:20:18.000+0000",        "valUnitarioUltimaVenda": 7.5,        "valUltimaVenda": 0.01,        "numCNPJ": "09326499000104",        "nomRazaoSocial": "SOTEL HOTELARIA S/A",        "nomFantasia": "SOTEL HOTELARIA",        "numTelefone": null,        "nomLogradouro": "AV DOUTOR ANTONIO GOUVEIA",        "numImovel": "925",        "nomBairro": "PAJUCARA",        "numCep": "57030170",        "nomMunicipio": "MACEIO",        "numLatitude": -9.6663527,        "numLongitude": -35.7125364    }]';
    return Scaffold(
      backgroundColor: Colors.white,

      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: SingleChildScrollView(
          padding: EdgeInsets.all(16.0),
          child: FutureBuilder(
            future: getProducts(description),
            builder: (context, snapshot) {
              if (snapshot.connectionState == ConnectionState.done) {
                var value = snapshot.data;
                print(value);
                return JsonTable(jsonDecode(jsinFucked));
              } else {
                return CircularProgressIndicator();
              }
            },
          )),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: 'Increment',
        child: Icon(Icons.favorite),
      ), // This trailing comma makes auto-formatting nicer for build methods.
    );
  }

  Future<List<ResponseJson>> getProducts(String description) async {
    String authority =
        "http://api.sefaz.al.gov.br/sfz_nfce_api/api/public/consultarPrecosPorDescricao";
    final url = Uri.parse("https://jsonplaceholder.typicode.com/posts");
    Map<String, String> headers = {
      "Content-type": "application/json"
      // "AppToken": token
    };
    String json =
        '{"descricao": $description, "dias": "3", "latitude": "-9.7510358", "longitude": "-36.6695834", "raio": "15"}';

    Response response = await post(url, headers: headers, body: json);

    List jsonResponse = jsonDecode(response.body);
    return jsonResponse.map((e) => new ResponseJson.fromJson(e)).toList();
  }

  DataTable showData(String description) {
    return DataTable(
      columns: const <DataColumn>[
        DataColumn(
          label: Text(
            'Descrição do Produto',
            style: TextStyle(fontStyle: FontStyle.italic),
          ),
        ),
        DataColumn(
          label: Text(
            'Valor última venda',
            style: TextStyle(fontStyle: FontStyle.italic),
          ),
        ),
        DataColumn(
          label: Text(
            'Estabelecimento',
            style: TextStyle(fontStyle: FontStyle.italic),
          ),
        ),
        DataColumn(
          label: Text(
            'Bairro',
            style: TextStyle(fontStyle: FontStyle.italic),
          ),
        ),
        DataColumn(
          label: Text(
            'Municipio',
            style: TextStyle(fontStyle: FontStyle.italic),
          ),
        ),
        DataColumn(
          label: Text(
            'CEP',
            style: TextStyle(fontStyle: FontStyle.italic),
          ),
        ),
      ],
      rows: data,
    );
  }
}
