import json

import requests

from .config import get_current_model
from .constants import OLLAMA_URL
from .memory import (
    add_message,
    get_messages,
    save_memory,
)
from .smart_memory import (
    get_memory,
    process_message,
)
from .system_prompt import SYSTEM_PROMPT


def build_system_prompt():
    smart_memory = get_memory()

    return (
        SYSTEM_PROMPT
        + "\n\n"
        + "User Memory:\n"
        + json.dumps(
            smart_memory,
            indent=2,
            ensure_ascii=False,
        )
    )


def chat_with_ai(message):
    process_message(message)

    add_message("user", message)

    messages = get_messages()

    messages = [
        {
            "role": "system",
            "content": build_system_prompt(),
        },
        *messages,
    ]

    response = requests.post(
        OLLAMA_URL,
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
