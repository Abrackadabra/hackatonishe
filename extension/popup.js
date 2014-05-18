$(document).ready(function(){
  $("#home").on('click', function() {
    chrome.tabs.create({'url': serverUrl});
  });

  chrome.runtime.sendMessage({query: "getnotifications"}, function(response) {
    if(response.notifications.length > 0) {
      var items = []
      $.each(response.notifications, function(key, value) {
        items.push('<li>User <b>' + value.name + '</b> saw that you downloaded <b>' + value.text + '</b> and wants to chat!<br><a class="chatlink" href="#" data-userkey="' + value.user + '">Accept</a></li>');
      });

      $('#notifications').html(items.join(''));


      $(".chatlink").on("click", function() {
        chrome.tabs.create({'url': serverUrl + '/chat/' + $(this).attr('data-userkey')});
        window.close();
      });
    } else {
      $('#notifications').html('No pending notifications.');
    }
  });
});
