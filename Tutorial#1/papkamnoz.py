import random

user_action = input("papier,kamień czy nożyce? ")
possible_actions = ["papier", "kamień", "nożyce"]
computer_action = random.choice(possible_actions)
print(f"\nWybrałeś {user_action}, a komputer wybrał {computer_action}.\n")

if user_action == computer_action:
    print(f"Gracz i komputer wybrali"
          f" {user_action}. Remis!")
elif user_action == "kamień":
    if computer_action == "nożyce":
        print("Kamień niszczy nożyce! Wygrywasz!")
    else:
        print("Papier pokrywa kamień! Przegrywasz.")
elif user_action == "papier":
    if computer_action == "kamień":
        print("Papier pokrywa Kamień! Wygrywasz!")
    else:
        print("Nożyce tną papier! Przegrywasz.")
elif user_action == "nożyce":
    if computer_action == "papier":
        print("Nożyce tną papier! Wygrywasz!")
    else:
        print("Kamień niszczy nożyce! Przegrywasz")
