import os
import asyncio
from typing import List
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from openai import AsyncOpenAI
import gradio as gr

# Import your agent framework (same as in your Travel Agent code)
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled

# 🔑 Load environment variables
load_dotenv()

BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")

if not BASE_URL or not API_KEY or not MODEL_NAME:
    raise ValueError("Please set BASE_URL, API_KEY, and MODEL_NAME in .env")

# ⚡ Initialize OpenAI Async Client
client = AsyncOpenAI(base_url=BASE_URL, api_key=API_KEY)
set_tracing_disabled(disabled=True)

# --- Output Model ---
class LinkedInPost(BaseModel):
    topic: str = Field(description="The topic of the LinkedIn post")
    language: str = Field(description="Language of the post (e.g., English, Bengali, Spanish)")
    content: str = Field(description="The generated LinkedIn post (2–4 paragraphs)")

# --- LinkedIn Post Agent ---
linkedin_agent = Agent(
    name="LinkedIn Post Writer",
    instructions="""
    You are an expert LinkedIn content writer.

    Task:
    - Write a professional LinkedIn post on the given topic.
    - The post should be engaging, structured, and 2–4 paragraphs long.
    - Always write in the language requested by the user.

    Style Guidelines:
    - Keep tone professional yet relatable.
    - Use short paragraphs for readability.
    - Avoid hashtags unless explicitly requested.
    - Do not use bullet points, keep it natural like a real LinkedIn post.
    """,
    model=OpenAIChatCompletionsModel(model=MODEL_NAME, openai_client=client),
    tools=[],   # no external tools needed
    output_type=LinkedInPost
)

# --- Async wrapper for Gradio ---
async def generate_post_async(topic: str, language: str):
    query = f"Generate a LinkedIn post about '{topic}' in {language}"
    result = await Runner.run(linkedin_agent, query)

    if hasattr(result.final_output, "content"):
        post = result.final_output
        formatted_output = (
            f"📝 **Topic**: {post.topic}\n\n"
            f"🌐 **Language**: {post.language}\n\n"
            f"💡 **LinkedIn Post**:\n\n{post.content}"
        )
        return formatted_output
    else:
        return str(result.final_output)

def generate_post(topic: str, language: str):
    return asyncio.run(generate_post_async(topic, language))

# --- Gradio Interface ---
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("## 🤖 AI LinkedIn Post Generator (Agent Framework)")
    gr.Markdown("Enter a **topic** and select a **language** to generate a LinkedIn-style post.")

    with gr.Row():
        topic_input = gr.Textbox(label="Topic", placeholder="e.g., AI in Healthcare")
        lang_input = gr.Dropdown(
            choices=["English", "Bengali", "Spanish", "French"],
            label="Language",
            value="English"
        )

    generate_btn = gr.Button("✨ Generate Post")
    output_box = gr.Markdown()

    generate_btn.click(fn=generate_post, inputs=[topic_input, lang_input], outputs=output_box)

# ▶️ Run Gradio App
if __name__ == "__main__":
    demo.launch()
