from .ai import chat_with_ai
from .config import MODEL_NAME


def main():
    print("=" * 40)
    print("👑 Welcome to Empire AI")
    print("=" * 40)

    name = input("\nEnter your name: ")

    while True:
        print(f"\nHello, {name}")
        print("\n1. Chat")
        print("2. About")
        print("3. Exit")

        choice = input("\nChoose: ")

        if choice == "1":
            print("\n🤖 Empire AI Chat")
            print("Type /exit to return to the menu.\n")

            while True:
                message = input("You: ")

                if message.lower() == "/exit":
                    print("\nLeaving chat...\n")
                    break

                print("\n🤖 Thinking...\n")

                reply = chat_with_ai(message)

                print(reply)
                print()

        elif choice == "2":
            print("\nEmpire AI")
            print("Version: 0.2")
            print(f"Current Model: {MODEL_NAME}")
            print("Built by Ahsan & ChatGPT")

        elif choice == "3":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid option.")


if __name__ == "__main__":
    main()
