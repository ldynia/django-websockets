#!/bin/sh

CONTAINER_IP=$(ip addr | grep inet | tail -n1 | awk '{print $2}' |  cut -d'/' -f1)
echo "Container IP: $CONTAINER_IP"

echo "Starting redis server"
redis-server --daemonize yes

echo "Install requirements.txt"
pip install -r /app/requirements.txt --no-cache-dir

echo "Run migrations"
python /app/manage.py makemigrations
python /app/manage.py migrate

# if args empty
if [ -z "$@" ]
then
    echo "Run Server"
    # python /app/manage.py runserver 0.0.0.0:$PORT
    # gunicorn config.wsgi:application -w 8 -b 0.0.0.0:$PORT
    daphne config.asgi:application -b 0.0.0.0 -p $PORT
else
    echo "Executeing \$@ command: $@"
    exec $@
fi