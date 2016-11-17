var express = require('express');
var app = express();

app.get('/', function (request, response) {
  response.send("Hello World");
});

app.listen(8080);