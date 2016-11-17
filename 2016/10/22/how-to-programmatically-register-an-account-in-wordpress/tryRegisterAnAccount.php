<?php
  // Include the wp-load.php so that we can use WordPress API
  $parse_uri = explode( 'wp-content', $_SERVER['SCRIPT_FILENAME'] );
  require_once( $parse_uri[0] . 'wp-load.php' );

  define("USERNAME_ALREADY_EXIST", 1);
  define("EMAIL_ADDRESS_ALREADY_EXIST", 2);
  define("NOT_A_VALID_EMAIL_ADDRESS", 3);
  define("PASSWORD_LENGTH_IS_TOO_SHORT", 4);
  define("SUCCESS", true);
  define("FAIL", false);

  $data = array();
  $errors = array();
  $username = sanitize_text_field($_POST['username']);
  $email = sanitize_text_field($_POST['email']);
  $password = sanitize_text_field($_POST['password']);

  $data["username"] = $username;
  $data["email"] = $email;
  $data["password"] = $password;

  if (!empty($username)) {
    if (username_exists($username)) {
      $errors[] = USERNAME_ALREADY_EXIST;
    }
  }

  if (!empty($email)) {
    if (!is_email($email)) {
      $errors[] = NOT_A_VALID_EMAIL_ADDRESS;
    }else{
      if (email_exists($email)) {
        $errors[] = EMAIL_ADDRESS_ALREADY_EXIST;
      }
    }
  }

  if (!empty($password)) {
    if (strlen($password) < 5) {
      $errors[] = PASSWORD_LENGTH_IS_TOO_SHORT;
    }
  }

  if (count($errors)) {
    $data["errors"] = $errors;
    $data["result"] = FAIL;
  }else{
    if (!empty($username) && !empty($email) && !empty($password)) {
      $random_password = wp_generate_password($length=12, $include_standard_special_chars=false);
      $userID = wp_create_user($username, $random_password, $email);
      if (!is_wp_error($user_id)) {
        wp_set_password($password, $userID);
        $data["result"] = SUCCESS;
      }else{
        $data["result"] = FAIL;
      }
    }else{
      $data["result"] = FAIL;
    }
  }

  // return all our data to an AJAX call
  echo json_encode($data, JSON_PRETTY_PRINT);
?>