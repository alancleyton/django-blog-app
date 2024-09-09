#!/bin/sh

set -e

while ! nc -z $DB_HOST $DB_PORT; do
  echo "🟡 Waiting for Postgres Database Startup ($DB_HOST $DB_PORT) ..." &
  sleep 3
done

echo "✅ Postgres Database Started Successfully ($DB_HOST:$DB_PORT)"

python manage.py collectstatic --noinput
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py runserver 0.0.0.0:8000
