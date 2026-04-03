include .env
export

export PROJECT_ROOT=${shell pwd}

start:
	make env-up
	make env-port-forward
	docker ps -a
	
stop:
	make env-down
	make env-port-close
	docker ps -a



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

