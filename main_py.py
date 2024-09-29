from game import *
from game_library import *
from user_account import *
from user_inventory import *
from rental_system import *

def main_menu():
    rental_system = RentalSystem()
    while True:
        print("\n Welcome to the rental Game System")
        print("1. Display Available Game")
        print("2. Register User")
        print("3. Log In")
        print("4. Admin Log In")
        print("5. Exit")
        choice = int(input("Enter your option: "))

        if choice == 1:
            rental_system.game_library.display_available_games()
        elif choice == 2:
            rental_system.register_user()
        elif choice == 3:
            username = input("Enter username: ")
            if rental_system.login(username):
                rental_system.logged_in_menu(username)
        elif choice == 4:
            rental_system.admin_login()
        elif choice == 5:
            print("Exiting Program...")
            break
        else:
            print("Invalid Output. Try another.")


if __name__ == "__main__":
    main_menu()