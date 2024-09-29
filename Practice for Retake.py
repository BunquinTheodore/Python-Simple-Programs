#Practice for Retake 

game_library = {
    "Mobie Legends" : {"Load" : 20, "Quantity" : 10},
    "Call of Duty" : {"Load": 30, "Quantity" : 5},
    "Naturo Shippuden" : {"Load" : 40, "Quantity" : 8}
}

user_accounts = {}
user_inventory = {}

def main():
    print ("Welcome to Game Library Management!")
    print ("1. Register")
    print ("2. Log-in")
    print ("3. Exit")
    while True:
        try:
            choice = int(input("Enter choice: "))
            if choice == 1:
                register()
            elif choice == 2:
                log_in()
            elif choice == 3:
                print ("Exiting Program...")
                break
            else:
                print ("Invalid Input")
                
        except ValueError as e:
            print (f"Error: {e}")

def register():
    while True: 
        register_name = input("Enter username: ")
        register_password = input("Enter password: ")
        if register_name in user_accounts: 
            print ("Account already used! Try another one \n")
            register()
        else:
            user_accounts[register_name] = {"password" : register_password, "Load" : 0}
            print ("Account Successfully Registered!")
            return()
        

def log_in():
    while True:
        try: 
            log_in_username = input("Enter username: ")
            log_in_password = input("Enter password: ")
            if log_in_username in user_accounts:
                if log_in_password == user_accounts[log_in_username]["password"]:
                    sub_menu(log_in_username)
                    break
                else:
                    print ("Wrong password")
            else:
                print ("Username not Found")
                exit = input("Press zero(0) to log out: ")
                if exit == 0:
                    break
        except ValueError and IndexError as e:
            print (f"Error: {e}")
        
def sub_menu(log_in_username):
    while True:
        print("Welcome to the Game Store!")
        print("1. Display Available Games")
        print("2. Rent Game")
        print("3. Return Game")
        print("4. Add Load")
        print("5. Display Inventory")
        print("6. Redeem Free Rental")
        print("7. Logout")
        choice = int(input("Enter choice: "))
        try:
            if choice == 1:
                display_available_games()
            elif choice == 2:
                rent_game(log_in_username)
            elif choice == 3:
                return_game()
            elif choice == 4:
                load = input ("Enter the desired load: ")
                add_load(log_in_username,load)
            elif choice == 5:
                display_inventory()
            elif choice == 6:
                redeem_free_rental()
            elif choice == 7:
                print("Logging out")
                return
            else:
                print("Invalid input!")
        except ValueError as e:
            print(f"Error: {e}")

def display_available_games():
    print ("Game Inventory: ")
    for game, info in game_library.items():
        print(f'{game} -  Load: {info["Load"]}, Quantity:{info["Quantity"]}')
    return

def rent_game(log_in_username):
    while True:
        print ("Renting Game")
        game = input ("Enter game you want to rent: ")
        if game in game_library and game_library[game]["Quantity"] > 0:
            cost = game_library[game]["Quantity"]
            if cost in game_library[log_in_username]["Load"] >= 0:
                user_inventory[log_in_username] = game
                game_library[game]["Quantity"] -= 1
                user_accounts[log_in_username]["Load"] -= cost
                print (f"You have successfullt rented the {game}!")
            else:
                print ("Insufficient Load Balance!")
        else: 
            print ("Game not available in game library")
            return 
        
def return_game(log_in_username):
    print ("Returning Game")
    game = input ("Enter game to be returned: ")
    if game in user_inventory:
        game = user_inventory.pop(log_in_username)
        game_library[game]["Quantity"] += 1
        print ("Game Returned Successfully!")
    else:
        print ("Game not in inventory!")

def add_load(log_in_username, load):
    print ("Adding Load")
    if log_in_username in user_accounts:
        user_accounts[log_in_username]["Load"] += load
        print ("You have been Loaded Successfully!")
    else:
        print ("User not found!")
        

def display_inventory(log_in_username):
    if log_in_username in user_accounts:
        for game in user_inventory:
            print (f"You have rented {game}")
            break
    else:
        print ("No game rented!")

def redeem_free_rental():
    print ("Redeeming Free Rental!")

main()