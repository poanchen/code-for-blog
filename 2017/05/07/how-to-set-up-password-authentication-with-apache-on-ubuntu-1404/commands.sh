sudo apt-get update
sudo apt-get install apache2 apache2-utils
sudo htpasswd -c /etc/apache2/.htpasswd username
cat /etc/apache2/.htpasswd
sudo vi /etc/apache2/sites-enabled/000-default.conf
sudo service apache2 restart