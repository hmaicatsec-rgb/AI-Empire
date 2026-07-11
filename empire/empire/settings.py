from .config import (
    AVAILABLE_MODELS,
    get_current_model,
    set_current_model,
)


def settings_menu():
    while True:
        print("\n========== Settings ==========")
        print(f"\nCurrent Model: {get_current_model()}")

        print("\nAvailable Models:\n")

        for index, model in enumerate(AVAILABLE_MODELS, start=1):
            print(f"{index}. {model}")

        print("\n0. Back")

        choice = input("\nChoose: ")

        if choice == "0":
            return

        if not choice.isdigit():
            print("\n❌ Invalid option.")
            continue

        choice = int(choice)

        if 1 <= choice <= len(AVAILABLE_MODELS):
            selected_model = AVAILABLE_MODELS[choice - 1]

            set_current_model(selected_model)

            print(f"\n✅ Model changed to: {selected_model}")

        else:
            print("\n❌ Invalid option.")
