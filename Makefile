dev_build:
	docker-compose -f docker-compose.yml build

dev_attach:
	docker-compose -f docker-compose.yml up

dev_migrate_db: dev_django_makemigrations dev_django_migrate

dev_django_makemigrations:
	docker exec -it django_test python manage.py makemigrations

dev_django_migrate:
	docker exec -it django_test python manage.py migrate