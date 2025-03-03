# Stock_price_ai

## Setup on Linux / WSL

1. clone the repository and navigate to the project directory
2. Make sure you have docker and docker-compose installed
3. Copy the .env.example file to .env and add your chatgpt key value
4. Run ```docker-compose build``` to build the app

## Run the app

1. Run ```docker-compose up``` to start the app
2. Open the browser on http://localhost:8501

## Run the tests

1. Run ```docker-compose up -d```
2. Run ```docker exec stock_price_ai-app-1 pytest``` to run the tests

