$(document).ready(function(){
  $("#home").on('click', function() {
    chrome.tabs.create({'url': serverUrl});
  });

  chrome.runtime.sendMessage({query: "getnotifications"}, function(response) {
      var items = []
      $.each(response.notifications, function(key, value) {
        items.push('<li>User <b>' + value.user + '</b> wants to chat!<br><a class="chatlink" href="#" data-userkey="' + value.user + '">Accept</a></li>');
      });

      $('#notifications').html(items.join(''));


      $(".chatlink").on("click", function() {
        chrome.tabs.create({'url': serverUrl + '/chat/' + $(this).attr('data-userkey')});
        window.close();
      });
    }
  );
});
