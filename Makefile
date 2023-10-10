attach:
  docker-compose up

build:
  docker-compose build

django_makemigrations:
  docker-compose exec django python manage.py makemigrations

django_migrate:
  docker-compose exec django python manage.py migrate