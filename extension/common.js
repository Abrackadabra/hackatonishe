//apiUrl = 'http://abra0.com:8000'
serverUrl = 'http://192.168.1.41:80'
apiUrl = 'http://192.168.1.41:8000'

function sendTorrentData(data) {
  $.ajax({
    type: "POST",
    url: apiUrl + '/torrent',
    data: data,
    success: function() {
      console.log('sent');
    }
  });
}
