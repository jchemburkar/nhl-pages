backend-build:
	docker build -f backend/docker/Dockerfile.uploader -t docker_uploader:latest .

backend-up:
	docker-compose -f backend/docker/docker-compose.yml up -d
	docker exec -it nhl_uploader python uploader/statsapi/upload_statsapi.py

backend-down:
	docker-compose -f backend/docker/docker-compose.yml down

backend-enter:
	docker exec -it nhl_uploader bash

database-enter:
	docker exec -it nhl_mysql mysql -uroot -pbeans