import os
import openai
import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage

# Load the variables from .env
load_dotenv()
# Access the API key
openai_api_key = os.getenv('OPENAI_API_KEY')
# Set the API key for OpenAI
openai.api_key = openai_api_key

# Your OpenAI API usage here

st.set_page_config(page_title="LangChain", page_icon=":globe_with_meridians:")
st.header("Hey there! I'm your Chatbot 🤖")

if "sessionMessages" not in st.session_state:
    st.session_state.sessionMessages = [SystemMessage(content="Hello! I'm your Chatbot 🤖")]
    
chat = ChatOpenAI(temperature=0.7, model= 'gpt-3.5-turbo')

def load_answer(question):
    st.session_state.sessionMessages.append(HumanMessage(content=question))
    assistant_answer = chat(st.session_state.sessionMessages)
    st.session_state.sessionMessages.append(AIMessage(content=assistant_answer.content))
    return assistant_answer.content

def get_text():
    input_text = st.text_input("Ask me anything!", key="input")
    return input_text

user_input = get_text()
submit = st.button("Generate Answer")
if submit:
    response = load_answer(user_input)
    st.subheader("Answer:")
    st.write(response, key=1)