import random

# ----------------------------
# STARTER PARALLEL ARRAYS (Part 1)
# ----------------------------
terms = [
    "LAN",
    "WAN",
    "Router",
    "Switch",
    "DNS",
    "Star topology",
    "Mesh topology"
]

definitions = [
    "A Local Area Network covering a small area, such as a home or school.",
    "A Wide Area Network covering a large area and connecting multiple LANs.",
    "A device that connects different networks and routes data between them.",
    "A device that connects devices on a LAN and sends data to the correct device.",
    "A system that translates domain names into IP addresses.",
    "A topology where all devices connect to a central device (hub/switch).",
    "A topology where devices are interconnected for high reliability."
]


# ----------------------------
# SUBPROGRAM 1: MENU
# ----------------------------
def show_menu():
    user_choice = ""
    while user_choice != "2":
        print("=== Networks Vocab Quiz (Part 1) ===")
        print("1. Start quiz")
        print("2. Exit")
        user_choice = input("Choose 1 or 2: ").strip()

        while user_choice != "1" and user_choice != "2":
            user_choice = input("Please choose 1 or 2: ").strip()

        if user_choice == "1":
            start_quiz(terms, definitions)
    print("\nGoodbye.\n")


# ----------------------------
# SUBPROGRAM 2: QUIZ LOOP
# ----------------------------
def start_quiz(term_list, definition_list):
    choice = "y"

    while choice == "y":
        i = random.randint(0, len(term_list) - 1)

        print("\nTerm:", term_list[i])
        input("Say the definition out loud, then press Enter to reveal the answer...")

        print("Definition:", definition_list[i])

        choice = input("\nAnother one? (y/n): ").strip().lower()
        while choice != "y" and choice != "n":
            choice = input("Please type y or n: ").strip().lower()

    print()


# ----------------------------
# MAIN PROGRAM LOOP
# ----------------------------
show_menu()
    


