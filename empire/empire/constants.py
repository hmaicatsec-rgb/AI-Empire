"""
Empire AI Constants

Never store private configuration in source code.
Configuration must come from .env.
"""

import os

from dotenv import load_dotenv

load_dotenv()

# ==========================
# Application
# ==========================

APP_NAME = os.getenv("APP_NAME")
APP_VERSION = os.getenv("APP_VERSION")

# ==========================
# AI
# ==========================

DEFAULT_MODEL = os.getenv("DEFAULT_MODEL")
OLLAMA_URL = os.getenv("OLLAMA_URL")

# ==========================
# Memory
# ==========================

MAX_MESSAGES = int(os.getenv("MAX_MESSAGES", "1000"))
CONTEXT_MESSAGES = int(os.getenv("CONTEXT_MESSAGES", "20"))

# ==========================
# Smart Memory
# ==========================

SMART_MEMORY_DIR = "empire"

FACTS_CATEGORY = "facts"
PREFERENCES_CATEGORY = "preferences"
PROFILE_CATEGORY = "profile"

# ==========================
# Encoding
# ==========================

DEFAULT_ENCODING = "utf-8"
