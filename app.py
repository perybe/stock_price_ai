import logging
from src.log import configure_logging
from dotenv import load_dotenv
import streamlit as st
from src.chatgpt import LangChainGpt
from src.stock_price import get_stock_price

load_dotenv()
configure_logging()


def start_chat_bot():
    st.title("💬 Chatbot")
    st.caption("Powered by OpenAI's gpt-4o-mini")
    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {"role": "assistant", "content": "Como posso lhe ajudar? / How can I help you?"}
        ]
        logging.info("App::Initialized Chatbot started and session state initialized.")


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
        logging.info(f"App::InputReceived User input received: {prompt}")
        try:
            response = gpt.chat_with_context(prompt)
            answer = response["answer"]
            stock_price, pct_change = get_stock_price(response["stock_locale"], response["stock"])
            if stock_price is not None:
                answer = answer.replace("{daily_price}", "{:.2f}".format(stock_price))
                answer = answer.replace("{pct_change}", "{:.2f}".format(pct_change))

            write_message("assistant", answer)
            logging.info(f"App::Response Assistant response: {answer}")
        except Exception as e:
            write_message("assistant", "I'm sorry, I couldn't find the stock you requested.")
            logging.error(f"App::Error Error getting stock price: {e}")


if __name__ == "__main__":
    main()
