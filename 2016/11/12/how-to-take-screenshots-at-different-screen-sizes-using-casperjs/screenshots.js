var casper = require("casper").create();
var fs = require('fs');
var urls = [];
var inputFile;
var contents;
var contentsToJSON;
var viewports = [
  {
    'name': 'Apple-iPhone-4s-portrait',
    'viewport': {width: 320, height: 480}
  },
  {
    'name': 'Apple-iPhone-4s-landscape',
    'viewport': {width: 480, height: 320}
  },
  {
    'name': 'Apple-iPhone-5-portrait',
    'viewport': {width: 320, height: 568}
  },
  {
    'name': 'Apple-iPhone-5-landscape',
    'viewport': {width: 568, height: 320}
  },
  {
    'name': 'Apple-iPhone-6-portrait',
    'viewport': {width: 540, height: 960}
  },
  {
    'name': 'Apple-iPhone-6-landscape',
    'viewport': {width: 960, height: 540}
  },
  {
    'name': 'Apple-iPad-mini-4-portrait',
    'viewport': {width: 768, height: 1024}
  },
  {
    'name': 'Apple-iPad-mini-4-landscape',
    'viewport': {width: 1024, height: 768}
  },
  {
    'name': 'Desktop-720p-HD',
    'viewport': {width: 1280, height: 720}
  },
  {
    'name': 'Desktop-1080p-HD',
    'viewport': {width: 1920, height: 1080}
  }
];

if (casper.cli.has(0)) {
  inputFile = casper.cli.get(0).toLowerCase();
}else{
  casper.echo("No file passed, aborting...").exit();
}

contents = fs.read(inputFile);
contentsToJSON = JSON.parse(contents);

var listOfLinks = contentsToJSON.links;
listOfLinks.forEach(function (currentValue, index, arr) {
  urls.push({url: currentValue.url});
});

casper.start().each(urls, function(self, link) {
  self.thenOpen(link.url, function() {
    var folderPath = 'screenshots/' + link.url.split('//')[1].split('/')[0] + '/';
    console.log("Taking screenshot for the url " + link.url + "...")
    viewports.forEach(function (currentValue) {
      console.log('Screenshot for ' + currentValue.name + ' (' + currentValue.viewport.width + 'x' + currentValue.viewport.height + ')', 'info');
      self.viewport(currentValue.viewport.width, currentValue.viewport.height);
      self.capture(folderPath + currentValue.name + '-' + currentValue.viewport.width + 'x' + currentValue.viewport.height + '.png', {
        top: 0,
        left: 0,
        width: currentValue.viewport.width,
        height: currentValue.viewport.height
      });
    });
  });
});

casper.run();