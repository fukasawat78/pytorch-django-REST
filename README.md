# pytorch-django


docker-compoe build
docker-compose up -d
docker exec -it backend bash

django-admin startproject core .
python manage.py startapp app

python manage.py makemigrations
python manage.py migrate

python manage.py runserver 0.0.0.0:8000