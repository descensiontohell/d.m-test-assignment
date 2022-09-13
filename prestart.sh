#!/bin/bash
sleep 3
cd gallery_backend
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
