install:
	docker-compose run --rm web pip install -r requirements-dev.txt --user --upgrade

start:
	docker-compose up web

daemon:
	docker-compose up -d web