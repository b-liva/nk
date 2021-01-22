#!/bin/sh
set -e
python3 manage.py collectstatic --noinput
uwsgi --socket :8000 --master --enable-threads --buffer-size=55535 --module nk.wsgi
