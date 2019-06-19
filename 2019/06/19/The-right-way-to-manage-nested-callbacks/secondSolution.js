// function get(url, header, param, success) {...}
// function post(url, header, param, success) {...}

var tokenType, accessToken, userId, playlistId, songs = JSON.parse(localStorage.songs);

retrieveAccessToken(function(response) {
  retrieveUserId(response, function(response) {
    createANewPlaylist(response, function(response) {
      addAllSongsToPlayList(response, function(total) {
        console.log("There are " + total + " out of " + songs.length + " songs been added to the playlist!!!");
      });
    });
  });
});

function retrieveAccessToken(callback) {
  post("https://accounts.spotify.com/api/token", {}, urlencode({
    grant_type: 'authorization_code',
    code: getParam(tab.url, 'code'),
    redirect_uri: "https://www.jenrenalcare.com/upload/thank-you.html",
    client_id: "3aa81ba3bbea466ba09fef04a5feea41",
    client_secret: "c47f40315044462d8b52bf747e8b2e1f"
  }), function(response) {
    callback(response);
  });
}

function retrieveUserId(response, callback) {
  tokenType = response.token_type;
  accessToken = response.access_token;
  get("https://api.spotify.com/v1/me", {
    Authorization: tokenType + ' ' + accessToken
  }, null, function(response) {
    callback(response);
  });
}

function createANewPlaylist(response, callback) {
  userId = response.id;
  post("https://api.spotify.com/v1/users/" + userId + "/playlists", {
    Authorization: tokenType + ' ' + accessToken,
    "Content-type": "application/json"
  }, JSON.stringify({
    name: localStorage.playlistTitle
  }), function(response) {
    callback(response);
  });
}

function searchASong(key, callback) {
  get("https://api.spotify.com/v1/search", {
    Authorization: tokenType + ' ' + accessToken
  }, "q=" + songs[key].title + "%20album:" + songs[key].album + "%20artist:" + songs[key].artist + "&type=track", function(response) {
    callback(response);
  });
}

function addASongToThePlaylist(uri, callback) {
  post("https://api.spotify.com/v1/users/" + userId + "/playlists/" + playlistId + "/tracks", {
    Authorization: tokenType + ' ' + accessToken,
    "Content-type": "application/json"
  }, JSON.stringify({
    uris: [uri]
  }), function(response) {
    callback(response);
  });
}

function addAllSongsToPlayList(response, callback) {
  playlistId = response.id;
  var i = 0;
  for (key in songs) {
    searchASong(key, function(response) {
      if (response.tracks.items.length) {
        addASongToThePlaylist(response.tracks.items[0].uri, function(response) {
          i++;
        });
      }
    });
  }
  callback(i);
}