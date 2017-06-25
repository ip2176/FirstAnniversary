python manage.py flush --noinput
python manage.py migrate --noinput
python manage.py createsuperuser --username admin --email admin@test.com --password testpass1 --noinput