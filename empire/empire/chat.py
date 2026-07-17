from .ai import chat_with_ai
from .memory import clear_messages, save_memory


def chat_menu():
    print("\n🤖 Empire AI Chat")
    print("Type /exit to return to the menu.\n")

    while True:
        message = input("You: ")

        if message.strip().lower() == "/exit":
            print("\nLeaving chat...\n")
            return

        if message.strip().lower() == "/clear":
            clear_messages()
            save_memory()

            print("\n✅ Memory cleared.\n")
            continue

        print("\n🤖 Thinking...\n")

        chat_with_ai(message)

        print()
