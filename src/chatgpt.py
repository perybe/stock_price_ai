from langchain.chat_models import init_chat_model
import os

class LangChainGpt:
    def __init__(self, model="gpt-4o-mini"):
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.client = init_chat_model(model, model_provider="openai")
        self.model = model

    def chat(self, messages):
        response = self.client.invoke(messages)
        msg = response.content
        return msg

    def chat_with_context(self, message):
        message_with_prompt = f"Gostaria que voce me criasse uma resposta para a pergunta '{message}'. A resposta precisa conter o simbolo da acao no comeco, separado por um espaco do resto da resposta.  Na resposta por favor criar uma frase com o valor do dia no formato {{cotacao_do_dia}}"
        return self.chat(message_with_prompt)


