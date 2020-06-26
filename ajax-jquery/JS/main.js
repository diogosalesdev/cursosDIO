function consultaCep() {
   $(".cep").hide();
  $(".animeprogressbar").show();
  var cep = document.getElementById("cep").value;
  console.log(cep);
  var url = "https://viacep.com.br/ws/"+cep+"/json/"
  console.log(url);
  $.ajax({
    url: url,
    type: "GET",
    success: function(res) {
      $(".animeprogressbar").hide();
      console.log(res);
      $("#logradouro").html(res.logradouro); //JQuery method
      $("#bairro").html(res.bairro); //JQuery method
      document.getElementById("cepibge").innerHTML = res.cep;
      document.getElementById("localidade").innerHTML = res.localidade;
      document.getElementById("uf").innerHTML = res.uf;
      $(".cep").show();
    }    
  })
}

//Using JQuery
$(function() {
  $(".cep").hide();
  $(".animeprogressbar").hide();
});

