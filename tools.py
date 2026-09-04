import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def record_unknown_question(question):
    with open("unknown_questions.txt", "a", encoding="utf-8") as f:
        f.write(f"Question: {question}\n\n")
    return {"status": "success", "message": "Unknown question recorded successfully."}


def record_user_details(email, name="Name not provided", notes="not provided"):
    with open("details.txt", "a", encoding="utf-8") as f:
        f.write(f"Email: {email}\nName: {name}\nNotes: {notes}\n\n")
    return {"status": "success", "message": "User details recorded successfully."}


record_user_details_json = {
    "name": "record_user_details",
    "description": "Use this tool to record that a user is interested in being in touch and provided an email address.",
    "parameters": {
        "type": "object",
        "properties": {
            "email": {"type": "string", "description": "The email address of this user"},
            "name": {"type": "string", "description": "The user's name, if provided"},
            "notes": {
                "type": "string",
                "description": "Context or details about the conversation",
            },
        },
        "required": ["email"],
        "additionalProperties": False,
    },
}

record_unknown_question_json = {
    "name": "record_unknown_question",
    "description": "Call this tool whenever the user asks a question that you cannot answer or lack information about.",
    "parameters": {
        "type": "object",
        "properties": {
            "question": {"type": "string", "description": "The unanswered question asked by the user"},
        },
        "required": ["question"],
        "additionalProperties": False,
    },
}

tools = [
    {"type": "function", "function": record_user_details_json},
    {"type": "function", "function": record_unknown_question_json},
]

tool_map = {
    "record_user_details": record_user_details,
    "record_unknown_question": record_unknown_question,
}


def handle_tool_calls(tool_calls):
    results = []
    for tool_call in tool_calls:
        tool_name = tool_call.function.name
        # Safely parse arguments whether they arrive as string or dict
        args_raw = tool_call.function.arguments
        arguments = json.loads(args_raw) if isinstance(args_raw, str) else args_raw
        
        print(f"Tool called: {tool_name}", flush=True)
        
        tool = tool_map.get(tool_name)
        if tool:
            result = tool(**arguments)
        else:
            result = f"Unknown tool: {tool_name}"

        results.append(
            {"role": "tool", "content": json.dumps(result), "tool_call_id": tool_call.id}
        )
    return results