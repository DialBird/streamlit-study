import streamlit as st
import pinecone

from langchain.llms import OpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.chat_models import ChatOpenAI

pinecone.init(api_key=st.secrets["pc_api_key"], environment=st.secrets["pc_env"])
index = pinecone.Index("rerankers")

st.title("🦜🔗 Langchain Quickstart App")

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"


def generate_response(input_text):
    chat = ChatOpenAI(temperature=0.7, openai_api_key=openai_api_key)
    messages = [
        SystemMessage(content="あなたは有能な日本人のアシスタントです"),
        HumanMessage(content=input_text),
    ]
    st.info(chat(messages))

with st.form("my_form"):
    text = st.text_area(
        "Enter text:", "What are 3 key advice for learning how to code?"
    )

    submitted = st.form_submit_button("Submit")
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
    elif submitted:
        generate_response(text)
