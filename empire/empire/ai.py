import subprocess

from .config import MODEL_NAME


def chat_with_ai(message):
    result = subprocess.run(
        ["ollama", "run", MODEL_NAME, message],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )

    return result.stdout.strip()
