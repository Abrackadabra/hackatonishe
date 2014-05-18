// register handler for magnet
$('a[href^="magnet:"]').on("click", function() {
  chrome.runtime.sendMessage({query: "getuserkey"}, function(response) {
    data = {
      'text': document.title,
      'link': window.location.href,
      'key': response.userKey
    };

    sendTorrentData(data);
  });
})

