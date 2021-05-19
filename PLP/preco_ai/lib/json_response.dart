class ResponseJson {
  String dscProduto;
  double valMinimoVendido;
  double valMaximoVendido;
  double valUnitarioUltimaVenda;
  String numCNPJ;
  String nomRazaoSocial;
  String nomBairro;
  String numCep;
  String nomMunicipio;

  ResponseJson(
      {this.dscProduto,
      this.valMinimoVendido,
      this.valMaximoVendido,
      this.valUnitarioUltimaVenda,
      this.numCNPJ,
      this.nomRazaoSocial,
      this.nomBairro,
      this.numCep,
      this.nomMunicipio});

  ResponseJson.fromJson(Map<String, dynamic> json) {
    dscProduto = json['dscProduto'];
    valMinimoVendido = json['valMinimoVendido'];
    valMaximoVendido = json['valMaximoVendido'];
    valUnitarioUltimaVenda = json['valUnitarioUltimaVenda'];
    numCNPJ = json['numCNPJ'];
    nomRazaoSocial = json['nomRazaoSocial'];
    nomBairro = json['nomBairro'];
    numCep = json['numCep'];
    nomMunicipio = json['nomMunicipio'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['dscProduto'] = this.dscProduto;
    data['valMinimoVendido'] = this.valMinimoVendido;
    data['valMaximoVendido'] = this.valMaximoVendido;
    data['valUnitarioUltimaVenda'] = this.valUnitarioUltimaVenda;
    data['numCNPJ'] = this.numCNPJ;
    data['nomRazaoSocial'] = this.nomRazaoSocial;
    data['nomBairro'] = this.nomBairro;
    data['numCep'] = this.numCep;
    data['nomMunicipio'] = this.nomMunicipio;
    return data;
  }
}
