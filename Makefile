# AllAtomic - Makefile
# Dev: @GhostMarshal | Channel: @ComputeCode
# (૨๑•̀ㅁ•́ฅा) Purple Anime Theme (#9A8CFF)

.PHONY: help install start stop restart clean docker build deploy heroku

# Variables
APP_NAME := AllAtomic
PYTHON := python3
PIP := pip3
DOCKER := docker

# Default target
help:
	@echo "$(APP_NAME) - Available Commands"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "  install    - Install dependencies"
	@echo "  start      - Start the bot"
	@echo "  stop       - Stop the bot"
	@echo "  restart    - Restart the bot"
	@echo "  clean      - Clean cache and temp files"
	@echo "  docker     - Build and run Docker image"
	@echo "  heroku     - Deploy to Heroku"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Install dependencies
install:
	@echo "$(APP_NAME) Installing dependencies..."
	$(PIP) install -r requirements.txt
	@echo "$(APP_NAME) Done!"

# Start the bot
start:
	@echo "$(APP_NAME) Starting..."
	$(PYTHON) -m $(APP_NAME)

# Stop the bot
stop:
	@echo "$(APP_NAME) Stopping..."
	@pkill -f "$(APP_NAME)" || true
	@echo "$(APP_NAME) Stopped!"

# Restart the bot
restart: stop start

# Clean cache and temp files
clean:
	@echo "$(APP_NAME) Cleaning..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type f -name "*.pyo" -delete 2>/dev/null || true
	find . -type f -name "*.pyd" -delete 2>/dev/null || true
	rm -rf .eggs/ 2>/dev/null || true
	rm -rf *.egg-info/ 2>/dev/null || true
	rm -rf build/ 2>/dev/null || true
	rm -rf dist/ 2>/dev/null || true
	rm -rf .pytest_cache/ 2>/dev/null || true
	rm -rf .coverage 2>/dev/null || true
	rm -rf htmlcov/ 2>/dev/null || true
	rm -rf logs/*.log 2>/dev/null || true
	@echo "$(APP_NAME) Cleaned!"

# Docker build and run
docker:
	@echo "$(APP_NAME) Building Docker image..."
	$(DOCKER) build -t $(APP_NAME) .
	@echo "$(APP_NAME) Running container..."
	$(DOCKER) run -d --name $(APP_NAME) -v $(shell pwd)/.env:/app/.env $(APP_NAME)
	@echo "$(APP_NAME) Container started!"

# Heroku deploy
heroku:
	@echo "$(APP_NAME) Deploying to Heroku..."
	git add .
	git commit -m "Update $(APP_NAME)"
	git push heroku main
	@echo "$(APP_NAME) Deployed!"

# Test
test:
	@echo "$(APP_NAME) Running tests..."
	pytest tests/ -v

# Lint
lint:
	@echo "$(APP_NAME) Linting..."
	flake8 .
	mypy .

# Format
format:
	@echo "$(APP_NAME) Formatting..."
	black .
	isort .

# Generate session
session:
	@echo "$(APP_NAME) Generating session..."
	$(PYTHON) generate_session.py

# Show status
status:
	@echo "$(APP_NAME) Status"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "  Version: 2.0.0"
	@echo "  Dev: @GhostMarshal"
	@echo "  Channel: @ComputeCode"
	@echo "  GitHub: https://github.com/corruptcrew/AllAtomic"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Update
update:
	@echo "$(APP_NAME) Updating..."
	$(PIP) install --upgrade -r requirements.txt
	@echo "$(APP_NAME) Updated!"

# Check requirements
check:
	@echo "$(APP_NAME) Checking requirements..."
	$(PIP) check
	@echo "$(APP_NAME) Checked!"

# Install in development mode
dev:
	$(PIP) install -e .

# Create virtual environment
venv:
	$(PYTHON) -m venv venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

# Activate venv
activate:
	@echo "Activate with: source venv/bin/activate"

# Show help
show-help:
	@$(MAKE) -pRrq : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'
