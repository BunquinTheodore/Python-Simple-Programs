# Practical Exam

game_library = {
    "Donkey Kong": {"quantity": 3, "cost": 2},
    "Super Mario Bros": {"quantity": 5, "cost": 3},
    "Tetris": {"quantity": 2, "cost": 1},
}

user_accounts = {}
user_inventory = {}

admin_username = "admin"
admin_password = "adminpass"

def display_available_games():
    print("Available Games:")
    for game, info in game_library.items():
        print(f"{game} - Quantity: {info['quantity']} - Cost: ${info['cost']}")

def register_user_input():
    username = input("Enter username: ")
    password = input("Enter password: ")
    user_accounts[username] = {"password": password, "balance": 0}
    print("User registered successfully.")

def rent_game(username):
    game = input("Enter the game you want to rent: ")
    if game in game_library and game_library[game]["quantity"] > 0:
        cost = game_library[game]["cost"]
        if user_accounts[username]["balance"] >= cost:
            user_inventory[username] = game
            user_accounts[username]["balance"] -= cost
            game_library[game]["quantity"] -= 1
            print(f"You have rented {game}. Remaining balance: ${user_accounts[username]['balance']}")
        else:
            print("Insufficient balance.")
    else:
        print("Game not available.")

def return_game(username):
    if username in user_inventory:
        game = user_inventory.pop(username)
        game_library[game]["quantity"] += 1
        print(f"{game} returned successfully.")
    else:
        print("No game rented.")

def top_up_account(username, amount):
    if username in user_accounts:
        user_accounts[username]["balance"] += amount
        print(f"Account topped up. New balance: ${user_accounts[username]['balance']}")
    else:
        print("User not found.")

def display_inventory(username):
    if username in user_inventory:
        print(f"Your rented game: {user_inventory[username]}")
    else:
        print("No game rented.")

def admin_update_game(game_name):
    if game_name in game_library:
        new_quantity = int(input(f"Enter new quantity for {game_name}: "))
        new_cost = float(input(f"Enter new cost for {game_name}: $"))
        game_library[game_name]["quantity"] = new_quantity
        game_library[game_name]["cost"] = new_cost
        print(f"{game_name} updated successfully.")
    else:
        print("Game not found.")

def admin_login():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    if username == admin_username and password == admin_password:
        admin_menu()
    else:
        print("Invalid credentials.")

def admin_menu():
    print("Admin Menu:")
    print("1. Update Game")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        game_name = input("Enter the game to update: ")
        admin_update_game(game_name)
    else:
        print("Invalid choice.")

def redeem_free_rental(username):
    if username in user_accounts:
        user_inventory[username] = "Free Game"
        print("You have redeemed a free rental.")
    else:
        print("User not found.")

def display_game_inventory():
    print("Game Inventory:")
    for game, info in game_library.items():
        print(f"{game} - Quantity: {info['quantity']} - Cost: ${info['cost']}")

def logged_in_menu(username):
    print(f"Welcome, {username}!")
    print("1. Display Available Games")
    print("2. Rent Game")
    print("3. Return Game")
    print("4. Top Up Account")
    print("5. Display Inventory")
    print("6. Redeem Free Rental")
    print("7. Logout")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        display_available_games()
    elif choice == 2:
        rent_game(username)
    elif choice == 3:
        return_game(username)
    elif choice == 4:
        amount = float(input("Enter amount to top up: $"))
        top_up_account(username, amount)
    elif choice == 5:
        display_inventory(username)
    elif choice == 6:
        redeem_free_rental(username)
    elif choice == 7:
        print("Logged out.")
    else:
        print("Invalid choice.")

def check_credentials(username, password):
    if username in user_accounts and user_accounts[username]["password"] == password:
        return True
    else:
        return False

def main():
    while True:
        print("Welcome to the Game Library Management System!")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            username = input("Enter username: ")
            password = input("Enter password: ")
            if check_credentials(username, password):
                if username == admin_username:
                    admin_login()
                else:
                    logged_in_menu(username)
            else:
                print("Invalid username or password.")
        elif choice == 2:
            register_user_input()
        elif choice == 3:
            print("Thank you for using the Game Library Management System!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
