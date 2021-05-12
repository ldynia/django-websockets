#!/bin/sh

CONTAINER_IP=$(ip addr | grep inet | tail -n1 | awk '{print $2}' |  cut -d'/' -f1)
echo "Container IP: $CONTAINER_IP"

echo "Install requirements.txt"
pip install -r /app/requirements.txt --no-cache-dir

# echo "Run migrations"
# python /app/manage.py migrate

# if args empty
if [ -z "$@" ]
then
    echo "Run Server"
    python /app/manage.py runserver 0.0.0.0:$PORT
else
    echo "Executeing \$@ command: $@"
    exec $@
fi