document.addEventListener("DOMContentLoaded", function(event) { 
  for (var i = 0; i < audio_array.length; i++) {
    addAudioToHTML(audio_array[i].artist, audio_array[i].title, audio_array[i].mp3, i);
  }

  function addAudioToHTML (artist, title, source, position) {
    var parentDiv = document.createElement("div");
    var firstP = document.createElement("p");
    var artistForP1 = document.createTextNode("Artist: " + artist);

    firstP.appendChild(artistForP1);
    parentDiv.appendChild(firstP);

    var secondP = document.createElement("p");
    var artistForP2 = document.createTextNode("Title: " + title);

    secondP.appendChild(artistForP2);
    parentDiv.appendChild(secondP);

    var audio = new Audio(source);
    audio.controls = true;
    // add warning message for web browser that does not support audio tag
    audio.innerHTML = "Your browser does not support the audio element.";

    parentDiv.appendChild(audio);

    var audioDiv = document.getElementById('audio');
    document.querySelector('#audio').insertBefore(parentDiv, audioDiv.childNodes[position]);
  }
});