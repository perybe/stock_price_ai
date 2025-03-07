import logging
from langchain.chat_models import init_chat_model
import os


class LangChainGpt:
    def __init__(self, model="gpt-4o-mini"):
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.client = init_chat_model(model, model_provider="openai")
        json_schema = {
            "title": "Chatbot",
            "description": "You are a chatbot that helps users with buying stocks. Your main focus is to return the symbol of the stock, the country of that stock and also a good answer to the question. Please respond in the language of the user.",
            "type": "object",
            "properties": {
                "stock": {
                    "type": "string",
                    "description": "Stock Symbol and return null if the stock is not found. if it's a BR stock, it should have the .SA suffix",
                },
                "stock_locale": {
                    "type": "string",
                    "description": "Stock locale. It should be ['us', 'br', undefined]",
                },
                "answer": {
                    "type": "string",
                    "description": "You should return an awesome answer to the users question. It should only return the value of today stocks and not any other days value. Include the value stock as {daily_price} in the place of the stock value and also the daily percentage change as {pct_change}%. If the stock is not found, return a normal answer to the users question. If the users asks for any stock value that isn't from today's date, please return that the stock value is not available.",
                },
            },
            "required": ["stock", "answer"],
        }
        self.structured_client = self.client.with_structured_output(json_schema)
        self.model = model

    def chat(self, messages):
        response = self.client.invoke(messages)
        msg = response.content
        logging.info(f"LangChainGPT::Response Chatbot response: {msg}")
        return msg

    def chat_with_context(self, message):
        response = self.structured_client.invoke(message)
        logging.info(f"LangChainGPT::Response Chatbot response: {response}")
        return response
