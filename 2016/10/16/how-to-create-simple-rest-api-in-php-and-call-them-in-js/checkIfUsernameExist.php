<?php
  // Include the wp-load.php so that we can use username_exists() function in WordPress API
  $parse_uri = explode( 'wp-content', $_SERVER['SCRIPT_FILENAME'] );
  require_once( $parse_uri[0] . 'wp-load.php' );

  $data = array();
  $username = sanitize_text_field($_POST['username']);

  if (username_exists($username)) {
    $data["username"] = $username;
    $data["result"] = true;
  }else {
    $data["username"] = $username;
    $data["result"] = false;
  }

  // return all our data to an AJAX call
  echo json_encode($data, JSON_PRETTY_PRINT);
?>