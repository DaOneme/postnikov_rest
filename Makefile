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
	fi
	docker compose run --rm postgres-migrate \
		-path /migrations \
		-database postgres://$(POSTGRES_USER):$(POSTGRES_PASSWORD)@postgres:5432/$(POSGRESS_DB)?sslmode=disable \
		up



env-port-forward:
	docker compose up -d port-forwarder

env-port-close:
	docker compose down port-forwarder



migrate-create:
	@if [ -z "$(seq)" ]; then \
		echo "нет параметра seq, make migrate-create seq=... " \
		exit 1; \
	fi; \
	docker compose run --rm postgres-migrate \
		create \
		-ext sql \
		-dir /migrations \
		-seq "$(seq)"

migrate-up:
	make migrate-action action=up

migrate-down:
	make migrate-action action=down

migrate-action:
	@if [ -z "$(action)" ]; then \
		echo "нет параметра action, make migrate-action action=... " \
		exit 1; \
	fi; \
	
	docker compose run --rm postgres-migrate \
		-path /migrations \
		-database postgres://$(POSTGRES_USER):$(POSTGRES_PASSWORD)@postgres:5432/$(POSTGRES_DB)?sslmode=disable \
		"$(action)"
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
	fi
	docker compose run --rm postgres-migrate \
		-path /migrations \
		-database postgres://$(POSTGRES_USER):$(POSTGRES_PASSWORD)@postgres:5432/$(POSGRESS_DB)?sslmode=disable \
		up



env-port-forward:
	docker compose up -d port-forwarder

env-port-close:
	docker compose down port-forwarder



migrate-create:
	@if [ -z "$(seq)" ]; then \
		echo "нет параметра seq, make migrate-create seq=... " \
		exit 1; \
	fi; \
	docker compose run --rm postgres-migrate \
		create \
		-ext sql \
		-dir /migrations \
		-seq "$(seq)"

migrate-up:
	make migrate-action action=up

migrate-down:
	make migrate-action action=down

migrate-action:
	@if [ -z "$(action)" ]; then \
		echo "нет параметра action, make migrate-action action=... " \
		exit 1; \
	fi; \
	
	docker compose run --rm postgres-migrate \
		-path /migrations \
		-database postgres://$(POSTGRES_USER):$(POSTGRES_PASSWORD)@postgres:5432/$(POSTGRES_DB)?sslmode=disable \
		"$(action)"
		