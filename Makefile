run-postgres:
	docker run --name llmask_postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d -v ./postgres-data:/var/lib/postgresql/data postgres
stop-postgres:	
	docker stop llmask_postgres
	docker rm llmask_postgres
