 cd /root/Flask_server/WOL_Flask_server
 nohup gunicorn --bind 0.0.0.0:8080 -w 4 app:app > flask_server_log.txt 2>&1 & exit