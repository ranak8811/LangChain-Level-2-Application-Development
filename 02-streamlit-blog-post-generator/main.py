import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain_core.prompts import PromptTemplate


st.set_page_config(
    page_title = "Blog Post Generator"
)

st.title("Blog Post Generator")

gemini_api_key = st.sidebar.text_input(
    "Gemini API Key",
    type = "password"
)

def generate_response(topic):
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7, google_api_key=gemini_api_key)
    template = """
    As experienced startup and venture capital writer, 
    generate a 400-word blog post about {topic}
    
    Your response should be in this format:
    First, print the blog post.
    Then, sum the total number of words on it and print the result like this: This post has X words.
    """
    prompt = PromptTemplate(
        input_variables = ["topic"],
        template = template
    )
    query = prompt.format(topic=topic)
    response = llm.invoke([HumanMessage(content=query)])
    return st.write(response.content)


topic_text = st.text_input("Enter topic: ")
if not gemini_api_key:
    st.warning("Enter Gemini API Key")
if gemini_api_key:
    generate_response(topic_text)
