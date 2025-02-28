from langchain.chat_models import init_chat_model
import os

class LangChainGpt:
    def __init__(self, model="gpt-4o-mini"):
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.client = init_chat_model(model, model_provider="openai")
        json_schema = {
            'title': 'Chatbot',
            'description': 'You are a chatbot that helps users with the buying stocks. Your main focus is to return the symbol of the stock and also a good answer to the question.',
            'type': "object",
            'properties': {
                'stock': {
                    'type': 'string',
                    'description':'Stock Symbol and return null if the stock is not found'},
                'answer': {
                    'type': 'string',
                    'description':'You should return an awesome answer to the user question with the value of the day in the format {cotacao_do_dia}. If the stock is not found, return a normal answer to the user question'}
            },
            "required": ["stock", "answer"],
        }
        self.structured_client = self.client.with_structured_output(json_schema)
        self.model = model

    def chat(self, messages):
        response = self.client.invoke(messages)
        msg = response.content
        return msg

    def chat_with_context(self, message):
        response = self.structured_client.invoke(message)
        return response



