#!/bin/sh
echo 'Running collectstatic'
python manage.py collectstatic --no-input --settings=Dante.settings.productions

echo 'Running connection db and migrate'
python manage.py wait_for_db --settings=Dante.settings.productions
python manage.py makemigrations --settings=Dante.settings.productions
python manage.py migrate --settings=Dante.settings.productions

echo 'Running gunicorn'
gunicorn --env DJANGO_SETTINGS_MODULE=Dante.settings.productions Dante.wsgi:application --bind 0.0.0.0:8000