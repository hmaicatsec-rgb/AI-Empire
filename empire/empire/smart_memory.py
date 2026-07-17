import json
import os
import re

from .constants import (
    DEFAULT_ENCODING,
    FACTS_CATEGORY,
    PREFERENCES_CATEGORY,
    PROFILE_CATEGORY,
    SMART_MEMORY_DIR,
)

current_user = ""
memory = {}


def create_memory():
    return {
        FACTS_CATEGORY: {},
        PREFERENCES_CATEGORY: {},
        PROFILE_CATEGORY: {},
    }


def get_smart_memory_file(name):
    return os.path.join(
        SMART_MEMORY_DIR,
        f"smart_memory_{name.lower()}.json",
    )


def load_smart_memory(name):
    global current_user
    global memory

    current_user = name

    memory_file = get_smart_memory_file(name)

    if os.path.exists(memory_file):
        with open(
            memory_file,
            "r",
            encoding=DEFAULT_ENCODING,
        ) as file:
            memory = json.load(file)

    else:
        memory = create_memory()
        save_smart_memory()

    memory.setdefault(FACTS_CATEGORY, {})
    memory.setdefault(PREFERENCES_CATEGORY, {})
    memory.setdefault(PROFILE_CATEGORY, {})


def save_smart_memory():
    with open(
        get_smart_memory_file(current_user),
        "w",
        encoding=DEFAULT_ENCODING,
    ) as file:
        json.dump(
            memory,
            file,
            indent=4,
            ensure_ascii=False,
        )


def get_memory():
    return memory


def remember_fact(key, value):
    memory[FACTS_CATEGORY][key] = value
    save_smart_memory()


def remember_preference(key, value):
    memory[PREFERENCES_CATEGORY][key] = value
    save_smart_memory()


def remember_profile(key, value):
    memory[PROFILE_CATEGORY][key] = value
    save_smart_memory()


def recall_fact(key):
    return memory[FACTS_CATEGORY].get(key)


def recall_preference(key):
    return memory[PREFERENCES_CATEGORY].get(key)


def recall_profile(key):
    return memory[PROFILE_CATEGORY].get(key)


def process_message(message):
    text = message.strip()

    patterns = [
        (
            r"my name is (.+)",
            lambda value: remember_fact(
                "name",
                value.strip(),
            ),
        ),
        (
            r"i live in (.+)",
            lambda value: remember_fact(
                "city",
                value.strip(),
            ),
        ),
        (
            r"my favourite color is (.+)",
            lambda value: remember_preference(
                "favorite_color",
                value.strip(),
            ),
        ),
        (
            r"my favourite programming language is (.+)",
            lambda value: remember_preference(
                "favorite_programming_language",
                value.strip(),
            ),
        ),
    ]

    for pattern, action in patterns:
        match = re.search(
            pattern,
            text,
            re.IGNORECASE,
        )

        if match:
            action(match.group(1))
            break
