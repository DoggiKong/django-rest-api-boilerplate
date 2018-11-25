build:
	docker-compose build

web:
	docker-compose up web
	
start:
	docker-compose up

daemon:
	docker-compose up -d