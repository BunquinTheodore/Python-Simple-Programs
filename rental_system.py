from user_inventory import *
from game_library import *
from user_account import *

class RentalSystem:
    def __init__(self):
        self.user_accounts = {}
        self.user_inventory = UserInventory()
        self.game_library = GameLibrary()

    def register_user(self):
        username = input("Enter your username: ")
        password = input("Enter password: ")
        self.user_accounts[username] = UserAccount(username, password, 0)
        print("Account registered successfully!")

    def login(self, username):
        if username in self.user_accounts:
            password = input("Enter your password: ")
            if password == self.user_accounts[username].password:
                return username
            else:
                print("Wrong password")
        else:
            print("Username not found")

    def rent_game(self, username):
        while True:
            game_name = input("Game to be rented: ")
            if game_name in self.game_library.games and self.game_library.games[game_name].quantity > 0:
                cost = self.game_library.games[game_name].cost
                if self.user_accounts[username].balance >= cost:
                    self.user_inventory.inventory[username] = game_name
                    self.game_library.games[game_name].quantity -= 1
                    self.user_accounts[username].balance -= cost
                    print(f"{game_name} rented successfully!")
                    return
            print("No game rented")

    def return_game(self, username):
        if username in self.user_inventory.inventory:
            game_name = self.user_inventory.inventory[username]
            self.game_library.games[game_name].quantity += 1
            self.user_inventory.inventory.pop(username)
            self.user_accounts[username].balance += self.game_library.games[game_name].cost
            print(f"{game_name} returned successfully.")
        else:
            print("No game rented")

    def top_up_account(self, username, amount):
        try:
            top_up_amount = float(input("Enter the amount to top-up: "))
            self.user_accounts[username].balance += top_up_amount
            print(f"Top-up successful! New balance: {self.user_accounts[username].balance}")
        except ValueError as e:
            print(f"Error: {e}")

    def admin_update_game(self, game_name):
        if game_name in self.game_library.games:
            new_quantity = int(input("Enter new quantity: "))
            new_cost = float(input("Enter new cost: "))
            self.game_library.games[game_name].quantity = new_quantity
            self.game_library.games[game_name].cost = new_cost
            print(f"{game_name} updated successfully!")
        else:
            print("Game not found!")

    def admin_login(self):
        username = input("Enter Admin Username: ")
        password = input("Enter Admin Password: ")
        if username == "Admin" and password == "adminpass":
            self.admin_menu()
        else:
            print("Invalid Credentials")

    def admin_menu(self):
        print("Admin Menu")
        print("1. Add/Update Games")
        choice = int(input("Enter Game to Update: "))
        if choice == 1:
            game_name = input("Enter game name: ")
            self.admin_update_game(game_name)
        else:
            print("Invalid Choice")

    def redeem_free_rental(self, username):
        pass

    def display_inventory(self, username):
        if username in self.user_inventory.inventory:
            print(f"You have rented game: {self.user_inventory.inventory[username]}")
        else:
            print("No games rented yet.")

    def logged_in_menu(self, username):
        print("Welcome to Log In Menu!")
        print("1. Rent a Game")
        print("2. Return a Game")
        print("3. Top up Account")
        print("4. Display Inventory")
        print("5. Redeem Free-rental")
        print("6. Log Out")
        choice = int(input("Enter choice: "))

        if choice == 1:
            self.rent_game(username)
        elif choice == 2:
            self.return_game(username)
        elif choice == 3:
            self.top_up_account(username, 0)
        elif choice == 4:
            self.display_inventory(username)
        elif choice == 5:
            self.redeem_free_rental(username)
        elif choice == 6:
            print("Exiting Program...")
            return
        else:
            print("Invalid Choice")
