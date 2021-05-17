# Description

This project demonstrate POC of how to married WebSockets with Django signals.

# Instructions

1.  Start application.

    ```bash
    $ git clone https://github.com/ldynia/django-websockets -b debian
    $ cd django-websockets
    $ git checkout tags/v1.0.0 -b POC
    $ docker-compose up
    ```

1. Open application    [http://localhost:8000/ws/models/person](http://localhost:8000/ws/models/person)

1. Open terminal and send message triggered by executing CLI command.

    ```bash
    $ docker exec -it django-demo-app ./manage.py demo
    ```