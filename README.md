# Stock_price_ai

## Setup on Linux / WSL

1. clone the repository and navigate to the project directory
2. Make sure you have docker and docker-compose installed
2. Run ```docker-compose build``` to build the app

## Run the app

1. Run ```docker-compose up``` to start the app
2. Open the browser on http://localhost:8501

## Run the tests

1. Run ```pytest```
1. Run ```pytest --cov-report term --cov=stock_price_ai tests/``` to get the coverage report

