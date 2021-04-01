web: gunicorn bookstore.wsgi
worker: celery -A bookstore worker -l INFO
release: python manage.py migrate --noinput
