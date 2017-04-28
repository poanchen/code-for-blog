var page = require('webpage').create();
var casper = require('casper').create();

var urlBeforeLoggedIn = "https://www.jenrenalcare.com/wp-login.php";
var urlAfterLoggedIn = "https://www.jenrenalcare.com/wp-admin/";

casper.start(urlBeforeLoggedIn);

casper.waitForSelector('form[method="post"]', function() {
  casper.fillSelectors('form[method="post"]', {
    'input[name="log"]': 'put_your_username_or_email_address_here',
    'input[name="pwd"]': 'put_your_password_here'
  }, true);
});

casper.waitForUrl(urlAfterLoggedIn, function() {
  this.viewport(3000, 1080);
  this.capture('./screenshot.png', {top: 0,left: 0,width: 3000, height: 1080});
});

casper.run();