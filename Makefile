backend-build:
	docker build -t nhl-pages-backend -f backend/Dockerfile .

backend-run:
	docker run --rm -it nhl-pages-backend:latest bash

backend-live-run:
	docker run -v ${PWD}/backend:/usr/src --rm -it nhl-pages-backend:latest bash