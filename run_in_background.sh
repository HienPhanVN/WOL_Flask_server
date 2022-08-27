 cd /root/Flask_server/WOL_Flask_server
 nohup waitress-serve --host 0.0.0.0 app:app > log.txt 2>&1 & exit