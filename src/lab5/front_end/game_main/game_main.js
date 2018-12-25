const baseUrl = 'http://127.0.0.1:5000/';

$(document).ready(function() {

  $.ajax(baseUrl + 'get_image?difficulty=' + $.urlParam('difficulty'), {
    success: function(src) {
      $("#person_to_guess_image").attr("src", src);
    },
    error: function(error) {
      console.log(error)
    }
  });

});

function submitGuess() {
  var answer = {answer: $("#input").val()};

  $.ajax ({
    type: 'POST',
    url: baseUrl + 'check_answer',
    contentType: 'application/json',
    data: JSON.stringify(answer),
    success: function (response) {
      result = response.result ? 'Верно!' : 'Неверно!';
      $("#answer_result").html(result);
    }
  })
}

$.urlParam = function(name){
  var results = new RegExp('[\?&]' + name + '=([^&#]*)').exec(window.location.href);
  if (results==null) {
     return null;
  }
  return decodeURI(results[1]) || 0;
}