syncdb:
	@python manage.py syncdb

runserver: syncdb
	@python manage.py runserver 0.0.0.0:8000

gera_staticos:
	@python manage.py collectstatic

test:
	@python manage.py test

syncb: deps
	@python manage.py syncdb

deps:
	@pip install -r requirements_env.txt

clean:
	@find . -iname "*.pyc" -delete
