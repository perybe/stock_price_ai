from dotenv import load_dotenv
import streamlit as st
from src.chatgpt import LangChainGpt
from src.stock_price import get_stock_price

load_dotenv()


def start_chat_bot():
    st.title("💬 Chatbot")
    st.caption("Powered by OpenAI's gpt-4o-mini")
    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {"role": "assistant", "content": "How can I help you?"}
        ]


def write_message(role, content):
    st.session_state.messages.append({"role": role, "content": content})
    st.chat_message(role).write(content)


def main():
    start_chat_bot()
    gpt = LangChainGpt()

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        write_message("user", prompt)

        response = gpt.chat_with_context(prompt)
        answer = response["answer"]
        stock_price = get_stock_price(response["stock"])
        if stock_price is not None:
            answer = answer.replace("{cotacao_do_dia}", "{:.2f}".format(stock_price))

        write_message("assistant", answer)


if __name__ == "__main__":
    main()
