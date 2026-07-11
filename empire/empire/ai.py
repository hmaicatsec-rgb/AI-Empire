import json

import requests

from .config import get_current_model
from .memory import (
    add_message,
    get_messages,
    save_memory,
)
from .system_prompt import SYSTEM_PROMPT


def chat_with_ai(message):
    add_message("user", message)

    messages = get_messages()

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        },
        *messages,
    ]

    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": get_current_model(),
            "messages": messages,
            "stream": True,
        },
        stream=True,
    )

    reply = ""

    for line in response.iter_lines(decode_unicode=True):
        if line:
            data = json.loads(line)

            content = data["message"]["content"]

            print(content, end="", flush=True)

            reply += content

    print()

    add_message("assistant", reply)

    save_memory()

    return ""
