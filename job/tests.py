from django.test import TestCase

# Create your tests here.


server {
    listen 80;
    server_name 34.67.77.187;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/almashnurmatk/hackaton;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}

sudo ln -s /etc/nginx/sites-available/hackaton /etc/nginx/sites-enabled



[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=almashnurmatk
Group=www-data
WorkingDirectory=/home/almashnurmatk/hackaton
ExecStart=/home//almashnurmatk/hackaton/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          hackaton.wsgi:application

[Install]
WantedBy=multi-user.target
