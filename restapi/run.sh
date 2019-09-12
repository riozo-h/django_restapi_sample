python manage.py makemigrations core product user cart
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn restapi.wsgi:application -b 0.0.0.0:8000
