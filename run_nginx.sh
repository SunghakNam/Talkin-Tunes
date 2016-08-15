#!/bin/bash
sudo /etc/init.d/nginx reload
sudo /etc/init.d/nginx start
uwsgi --socket :8001 --module shnam.wsgi
