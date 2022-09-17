#!/bin/bash
sleep 3
cd gallery_backend
python manage.py migrate

if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    python manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_EMAIL
fi

$@

gunicorn gallery_backend.wsgi:application --bind 0.0.0.0:8000
