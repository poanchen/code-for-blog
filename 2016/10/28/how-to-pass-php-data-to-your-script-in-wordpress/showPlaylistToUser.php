<?php
  // Include this php file, so that we have all the information for the audio that we will be playing later
  require_once("audioPlaylist.php");

  // Enqueue this js file, so that WordPress knows that we will be using this js file in this page
  wp_enqueue_script('audio-demo-player', get_template_directory_uri() . '/createPlaylist.js');

  // now we need to set the array name to be audio_array, so that later in the js file we can call them with that name
  // we also pass in the array that we have in the require_once
  wp_localize_script('audio-demo-player', 'audio_array', $urlsForAllTheAudios);

  // this trigger the <head></head> section, which will enqueue the js file. Without this, the js file will not be
  // included in this specific page
  wp_head();
?>

<div id="audio"></div>