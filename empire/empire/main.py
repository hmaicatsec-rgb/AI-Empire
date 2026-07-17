from .chat import chat_menu
from .config import get_current_model
from .memory import load_memory
from .settings import settings_menu
from .smart_memory import load_smart_memory


def main():
    print("=" * 40)
    print("👑 Welcome to Empire AI")
    print("=" * 40)

    name = input("\nEnter your name: ").strip()

    load_memory(name)
    load_smart_memory(name)

    while True:
        print(f"\nHello, {name}")
        print("\n1. Chat")
        print("2. About")
        print("3. Settings")
        print("4. Exit")

        choice = input("\nChoose: ")

        if choice == "1":
            chat_menu()

        elif choice == "2":
            print("\nEmpire AI")
            print("Version: 0.5")
            print(f"Current Model: {get_current_model()}")
            print("Built by Ahsan")

        elif choice == "3":
            settings_menu()

        elif choice == "4":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid option.")


if __name__ == "__main__":
    main()
