APP = devops-api

test:
	@flake8 . --exclude .venv
	@pytest -v --disable-warnings
compose: test
	@docker compose build
	@docker compose up
heroku:
	@heroku container:login
	@heroku container:push web -a $(APP)
	@heroku container:release -a $(APP) web