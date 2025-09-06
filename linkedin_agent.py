import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
import gradio as gr

# Load API key
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize LLM
llm = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY,
    model_name="gpt-4o-mini",  # or gpt-3.5-turbo
    temperature=0.7
)

# Define prompt template
prompt_template = """
You are a professional LinkedIn content creator.
Write a LinkedIn post about the topic: "{topic}".
Use the language: "{language}".
Make it structured, engaging, and professional in 2-4 paragraphs.
"""

chat_prompt = ChatPromptTemplate.from_template(prompt_template)
llm_chain = LLMChain(llm=llm, prompt=chat_prompt)

# Function to generate LinkedIn post
def generate_linkedin_post(topic: str, language: str):
    return llm_chain.run({"topic": topic, "language": language})

# Gradio Interface
interface = gr.Interface(
    fn=generate_linkedin_post,
    inputs=[
        gr.Textbox(label="Topic", placeholder="e.g., AI in Healthcare"),
        gr.Dropdown(label="Language", choices=["English", "Bengali", "Spanish"], value="English")
    ],
    outputs=gr.Textbox(label="Generated LinkedIn Post"),
    title="AI LinkedIn Post Generator",
    description="Generate professional LinkedIn posts in multiple languages using AI."
)

if _name_ == "_main_":
    interface.launch()
