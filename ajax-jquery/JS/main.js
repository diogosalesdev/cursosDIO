function consultaCep() {
  var cep = document.getElementById("cep").value;
  console.log(cep);
  var url = "https://viacep.com.br/ws/"+cep+"/json/"
  console.log(url);
  $.ajax({
    url: url,
    type: "GET",
    success: function(res) {
      console.log(res);
      document.getElementById("logradouro").innerHTML = res.logradouro;
      document.getElementById("bairro").innerHTML = res.bairro;
      document.getElementById("cepibge").innerHTML = res.cep;
      document.getElementById("localidade").innerHTML = res.localidade;
      document.getElementById("uf").innerHTML = res.uf;
    }
  })
}