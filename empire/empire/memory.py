import json
import os

from .constants import (
    CONTEXT_MESSAGES,
    DEFAULT_ENCODING,
    MAX_MESSAGES,
)

current_user = ""
messages = []


def get_memory_file(name):
    return f"empire/memory_{name.lower()}.json"


def get_messages():
    return messages[-CONTEXT_MESSAGES:]


def get_all_messages():
    return messages


def add_message(role, content):
    if len(messages) >= MAX_MESSAGES:
        messages.pop(0)

    messages.append(
        {
            "role": role,
            "content": content,
        }
    )


def clear_messages():
    global messages

    messages = []


def save_memory():
    with open(
        get_memory_file(current_user),
        "w",
        encoding=DEFAULT_ENCODING,
    ) as file:
        json.dump(
            messages,
            file,
            indent=4,
            ensure_ascii=False,
        )


def load_memory(name):
    global current_user
    global messages

    current_user = name

    memory_file = get_memory_file(name)

    if os.path.exists(memory_file):
        with open(
            memory_file,
            "r",
            encoding=DEFAULT_ENCODING,
        ) as file:
            messages = json.load(file)
    else:
        messages = []
