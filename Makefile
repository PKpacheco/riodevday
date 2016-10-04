clean:
	find . -name "*.pyc" -exec rm -rf {} \;
run: clean
	python3 manage.py runserver 0.0.0.0:8000 --settings=riodevday.settings
migrate:
	python3 manage.py migrate --settings=riodevday.settings
migrations:
	python3 manage.py makemigrations --settings=riodevday.settings
install:
	npm install
	bower install
	pip install -r requirements.txt
	make migrate
user:
	python3 manage.py createsuperuser --settings=riodevday.settings

shell:
	python3 manage.py shell --settings=riodevday.settings


