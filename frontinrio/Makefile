runserver: syncdb
	@python manage.py runserver 0.0.0.0:8000

test:
	@python manage.py test

syncb: deps
	@python manage.py syncdb

deps:
	@pip install -r requirements.txt

clean:
	@find . -iname "*.pyc" -delete
