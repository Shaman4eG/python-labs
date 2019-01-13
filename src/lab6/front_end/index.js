const baseUrl = 'http://127.0.0.1:5000/';

function getRssFeed() {
  var link = {link: $("#input").val()};

  $.ajax ({
    type: 'POST',
    url: baseUrl + 'cache_rss_and_return_it',
    contentType: 'application/json',
    data: JSON.stringify(link),
    success: function (response) {
      $.each(response.articles, function (index, value) {
        $('.container').append(
          '<div class="article">' +
            '<a class="header" href="' + value[2] + '">' + value[1] + '</a>' +
            '<div class="description">' + value[3] + '</div>' +
          '</div>'
        )
      })
    }
  });
}

$.urlParam = function(name){
  var results = new RegExp('[\?&]' + name + '=([^&#]*)').exec(window.location.href);
  if (results==null) {
     return null;
  }
  return decodeURI(results[1]) || 0;
}