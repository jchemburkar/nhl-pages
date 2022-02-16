# backend (python) cmds
backend-build:
	docker build -f backend/docker/Dockerfile.uploader -t docker_uploader:latest .

backend-up:
	docker-compose -f backend/docker/docker-compose.yml up -d
	sleep 5
	docker exec -it nhl_uploader python uploader/statsapi/upload_statsapi.py

api-start:
	docker exec -d nhl_uploader python api/app.py

backend-down:
	docker-compose -f backend/docker/docker-compose.yml down

backend-bounce: backend-down backend-up

backend-enter:
	docker exec -it nhl_uploader bash

# database cmds
database-enter:
	docker exec -it nhl_mysql mysql -uroot -pbeans

# frontend cmds
app-start:
	NODE_OPTIONS=--openssl-legacy-provider npm start --prefix apps

app-stop:
	npm stop --prefix apps

# full stack cmds
up: backend-up api-start app-start
down: backend-down app-stop