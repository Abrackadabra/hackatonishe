if (typeof String.prototype.startsWith != 'function') {
  // see below for better implementation!
  String.prototype.startsWith = function (str){
    return this.indexOf(str) == 0;
  };
}

// on extension load:
userKey = '';
chrome.cookies.get(
  {
    'url': 'http://192.168.43.180',
    'name': 'key'
  },
  function(data) {
    if(data) {
      userKey = data.value;
    } else {
      $.get(
        apiUrl + '/register',
        function (response) {
          userKey = response;
          chrome.cookies.set(
            {
              'url': 'http://192.168.43.180',
              'name': 'key',
              'value': response
            },
            function(data) {
              console.log(data);
            }
          );
        }
      );
    }
  }
);

// register handler for .torrent
pendingDownloads = {}
chrome.downloads.onCreated.addListener(function (downloadItem) {
  if(downloadItem.mime === 'application/x-bittorrent') {
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
      tab = tabs[0];

      pendingDownloads[downloadItem.id] = {
        'text': tab.title,
        'link': tab.url,
        'key': userKey
      };
    });
  }
})

chrome.downloads.onChanged.addListener(function(downloadDelta) {
  if(downloadDelta.id in pendingDownloads && downloadDelta.state && downloadDelta.state.current === 'complete') {
    sendTorrentData(pendingDownloads[downloadDelta.id]);
    delete pendingDownloads[downloadDelta.id];
  }
});

// register handler for magnet: see magnet.js
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  if (request.query === 'getuserkey') {
    sendResponse({
      userKey: userKey
    });
  }
});

// notifications
chrome.alarms.create(
  'pull_notifications_1',
  {
    'when': Date.now() + 0*15*1000,
    'periodInMinutes': 1
  }
);
chrome.alarms.create(
  'pull_notifications_2',
  {
    'when': Date.now() + 1*15*1000,
    'periodInMinutes': 1
  }
);
chrome.alarms.create(
  'pull_notifications_3',
  {
    'when': Date.now() + 2*15*1000,
    'periodInMinutes': 1
  }
);
chrome.alarms.create(
  'pull_notifications_4',
  {
    'when': Date.now() + 3*15*1000,
    'periodInMinutes': 1
  }
);

//pendingNotifications = [{'name': 'Big Brother', 'text': 'pron'}]
pendingNotifications = []

chrome.alarms.onAlarm.addListener(function(alarm) {
  if(alarm.name.startsWith('pull_notifications_')) {
    $.ajax({
      dataType: 'json',
      type: "GET",
      url: apiUrl + '/notifications',
      data: {
        key: userKey
      },
      success: function(data) {
        console.log('notifications get');
        pendingNotifications = pendingNotifications.concat(data.notifications);

        chrome.browserAction.setBadgeText({'text': pendingNotifications.length.toString()});
      }
    });
  }
})

// popup
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  if (request.query === 'getnotifications') {
    sendResponse({
      notifications: pendingNotifications
    });
  }
});
