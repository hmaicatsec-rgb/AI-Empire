import subprocess


def chat_with_ai(message: str) -> str:
    result = subprocess.run(
        ["ollama", "run", "qwen2.5-coder:7b", message],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )

    return result.stdout.strip()
