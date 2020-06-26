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
    }
  })
}