# Stock_price_ai

This app is a chatbot where you can ask for stock prices and get a response with the current stock price.

## Features

- Ask for the current stock price of various companies.
- Get the daily percentage change of the stock price.
- Supports multiple stock exchanges:
    - Brazil (B3)
    - United States (NYSE, NASDAQ)
- Supports multiple languages:
    - English
    - Portuguese
- Utilizes the ChatGPT API to generate responses, but could be changed to use a different API or a custom model with
  ease.
- Uses the Yahoo Finance API to get the stock prices.
- Uses Docker and Docker Compose to run the app in any environment.
- Has logging and tests to ensure the app is working as expected.

## Setup on Linux / WSL

1. clone the repository and navigate to the project directory
2. Make sure you have docker and docker-compose installed
3. Copy the .env.example file to .env and add your chatgpt key value to it.
4. Run ```docker-compose build``` to build the app

## Run the app

1. Run ```docker-compose up``` to start the app
2. Open the browser on http://localhost:8501

## Run the tests

1. Run ```docker-compose up -d```
2. Run ```docker exec stock_price_ai-app-1 pytest``` to run the tests

## Backlog

- Add more tests
- Add support to other stock exchanges
- Add support to other languages
    - Add a dropdown to select the language
- Add Support to other finance APIs