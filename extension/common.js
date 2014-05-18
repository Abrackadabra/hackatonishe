serverUrl = 'http://abra0.com'
apiUrl = 'http://abra0.com'
//serverUrl = 'http://192.168.1.41'
//apiUrl = 'http://192.168.1.41:8000'

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
