include .env
export


# Docker
d_b_run: docker_build docker_run

d_run: docker_run
docker_run:
	docker run -it --env-file .env -v $(pwd):/user_bot user_bot

d_b: docker_build
docker_build:
	docker build -t user_bot .


## Format all
fmt: format
format: isort black


## Check code quality
chk: check
lint: check
check: flake black_check isort_check

mypy:
	mypy app

## Sort imports
isort:
	isort app tests

isort_check:
	isort --check-only app


## Format code
black:
	black --config pyproject.toml app

black_check:
	black --config pyproject.toml --diff --check app


# Check pep8
flake:
	flake8 --config .flake8 app

