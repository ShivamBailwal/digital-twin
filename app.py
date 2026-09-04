from openai import OpenAI
from context import TWIN_SYSTEM_PROMPT
from tools import tools, handle_tool_calls
from styles import CSS, JS, EXAMPLES
from dotenv import load_dotenv
import gradio as gr
import os

load_dotenv(override=True)

gemini_api_key = os.getenv('GEMINI_API_KEY')
MODEL_NAME = "gemini-3.5-flash-lite"  # or "gemini-3.5-turbo" for the non-extended version

openai=OpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

system = [{"role": "system", "content": TWIN_SYSTEM_PROMPT}]

def chat(message,history):
    messages= system + history + [{"role": "user", "content": message}]
    response = openai.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        tools=tools,
    )
    while response.choices[0].finish_reason == "tool_calls":
        message=response.choices[0].message
        tool_calls=message.tool_calls
        results=handle_tool_calls(tool_calls)
        messages.append(message)
        messages.extend(results)
        response = openai.chat.completions.create(model=MODEL_NAME, messages=messages, tools=tools)
    return response.choices[0].message.content

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))

    gr.ChatInterface(
        chat,
        examples=EXAMPLES,
        title="Digital Twin",
        description="Talk to my AI twin about my career",
        chatbot=gr.Chatbot(show_label=False),
    ).launch(
        css=CSS,
        js=JS,
        theme=gr.themes.Base(),
        server_name="0.0.0.0",
        server_port=port,
    )
