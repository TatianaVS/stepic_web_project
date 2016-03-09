sudo /etc/init.d/mysql restart
mysql -uroot -e "CREATE DATABASE box_django;" 
python /home/box/web/ask/manage.py syncdb
