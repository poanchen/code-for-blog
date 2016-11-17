#!/bin/bash

curl http://PRIVATE_IP_ADDRESS:PORT_THAT_Node_JS_APP_LISTEN
sudo pm2 install pm2 -g
sudo pm2 YOUR_NODE_JS_SERVER_NAME_FILE.js
sudo pm2 list
sudo pm2 startup ubuntu
sudo apt-get update
sudo apt-get install apache2
sudo service apache2 status
sudo service apache2 start
cd /etc/apache2/sites-enabled/
sudo vi 000-default.conf
sudo service apache2 restart