include .env
export

export PROJECT_ROOT=${shell pwd}

start:
	make env-up
	make deploy
	docker ps -a

start-dev:
	make env-up
	make env-port-forward
	docker ps -a

stop:
	docker compose down -v 
	docker ps -a


deploy:
	docker compose up -d --build app

env-up:
	docker compose up -d postgres

env-down:
	docker compose down postgres

env-cleanup:
	@read -p "Очистить весь volume? Пизда данным >>> y/n  " answer; \
	if [ "$$answer" = "y" ]; then \
		docker compose down postgres && \
		sudo rm -rf out/pgdata && \
		echo "почищенно"; \
	else \
		echo "отбой"; \
	fi; 


env-port-forward:
	docker compose up -d port-forwarder

env-port-close:
	docker compose down port-forwarder

