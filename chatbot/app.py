from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os 
from dotenv import load_dotenv 

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
## LangSmith Tracing
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are an assistant, please respond to the queries"),
        ("user","Question: {question}")
    ]
)
## Streamlit Framework.
st.title("LangChain Demo with OpenAI API")
input_text = st.text_input("Search the topic you want")

## OpenAI LLM
llm = ChatOpenAI(model = "gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser 

if input_text:
    st.write(chain.invoke({"question":input_text}))




