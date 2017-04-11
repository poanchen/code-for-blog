<?php
  function does_file_exists($filename) {
    global $wpdb;
    
    return intval( $wpdb->get_var( "SELECT post_id FROM {$wpdb->postmeta} WHERE meta_value LIKE '%/$filename'" ) );
  }

  if ( null == ( $thumb_id = does_file_exists( 'example.png' ) ) ) {
    // hummm....seems like we have never seen this file name before, let's do an upload
  } else {
    // nice...the image already exist!!!
  }
?>