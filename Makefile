APP = restapi

test:
	@flake8 . --exclude .venv
	@pytest -v --disable-warnings
compose: test
	@docker compose build
	@docker compose up
heroku:
	@heroku container:login
	@heroku container:push web -a devops-api
	@heroku container:release -a devops-api web