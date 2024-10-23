# Variables
PYTHON = python3
PIP = pip
ENV_DIR = venv
SRC_DIR = src
TEST_DIR = tests
ENV_ACTIVATE = . $(ENV_DIR)/bin/activate

# Targets
.PHONY: all setup install run test lint clean

# Default target: runs the main program
all: run

# Set up the virtual environment
setup:
	$(PYTHON) -m venv $(ENV_DIR)

# Install dependencies from requirements.txt
install: setup
	$(ENV_ACTIVATE) && $(PIP) install -r requirements.txt

# Run the main application
run: install
	$(ENV_ACTIVATE) && $(PYTHON) $(SRC_DIR)/main.py

# Run tests
test:
	$(ENV_ACTIVATE) && pytest $(TEST_DIR)
