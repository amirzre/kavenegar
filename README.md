# Kavenegar API Integration

This project is a Python-based integration with the [Kavenegar](https://kavenegar.com/rest.html) SMS and Call API. It allows you to send SMS, check delivery status, manage accounts, and more using Kavenegar's services via an asynchronous interface built with `aiohttp`.

## Project Structure

```bash
kavenegar
├── LICENSE
├── README.md
├── requirements.txt
├── src
│   ├── config.py         # Configuration for API and environment variables
│   ├── exception.py      # Custom exceptions for API errors
│   ├── kavenegar.py      # Main Kavenegar API integration
│   ├── main.py           # Main script to send SMS
│   ├── __init__.py       # Package initialization
├── tests
│   └── test_kavenegar.py # Unit tests for Kavenegar API
└── Makefile              # Makefile for automating tasks
```

## Features
- Send SMS: The main functionality of the project is to send an SMS through Kavenegar’s API.
- Error Handling: The project includes custom exceptions for handling API-specific errors like APIException and HTTPException.
- Async Requests: API calls are asynchronous, using aiohttp for improved performance when interacting with the API.

## Prerequisites
- Python 3.10+
- virtualenv (recommended but optional)
You will also need to have the following environment variables set, preferably by creating a .env file in the root of the project:

```bash
KAVENEGAR_API_KEY=<your_kavenegar_api_key>
SENDER_NUMBER=<your_sender_number>
RECEPTOR_NUMBER=<your_receptor_number>
```

## Installation

1. Set up the virtual environment and install dependencies:
```bash
make install
```
This will create a Python virtual environment in the venv directory and install all necessary packages.

2. Add your environment variables by creating a .env file:
```bash
cp .env.sample .env
```
Add the following keys and values (replace with your actual credentials):
```bash
KAVENEGAR_API_KEY=your_kavenegar_api_key
SENDER_NUMBER=your_sender_number
RECEPTOR_NUMBER=your_receptor_number
```

## Running the Project

After the setup is complete, you can run the main script, which sends an SMS using Kavenegar's API:
```bash
make run
```
This will execute the script located at src/main.py, which sends an SMS based on the environment variables you’ve set in the .env file.

## Running Tests

To run the unit tests for the project, use:
```bash
make test
```
