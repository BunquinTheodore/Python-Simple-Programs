#BUILDING PROGRAM 3

bank_acc = {}

def create_acc():
    print("Create Account")
    while True:
        try:
            username = input("Enter username (or leave to go back): ")
            if not username:
                return
            if username in bank_acc:
                print("Username already exists. Enter another username.")
                continue
            password = input("Enter password (or leave to go back): ")
            balance = 0
            bank_acc[username] = {"password": password, "balance": balance}
            print("Account created successful!")
            break
        except ValueError as e:
            print (e)

def log_in():
    print("Log-In")
    while True:
        try:
            username = input("Enter username (or leave to go back): ")
            password = input("Enter password: ")
            if not username:
                return
            if bank_acc.get(username) and bank_acc[username]["password"] == password:
                print("Log-in succefully!")
                break
            else:
                print("Invalid username or password")
        except ValueError as e:
            print(e)

def withdraw(username):
    print("Withdraw")
    while True:
        try:
            print(f"Username: {username}, Balance: {bank_acc[username]['balance']}") 
            if bank_acc[username]['balance'] <= 0:
                print("Insufficient balnce!")
            else:
                withdraw_amount = float(input("Enter the amount to withdraw: "))
                bank_acc[username]['balance'] -= withdraw_amount
                print("Wiithdraw Successful!")
                print(f"New Balnace: {bank_acc[username]['balance']}")
        except ValueError as e:
            print(e)
        
def deposit(username):
    print("Deposit")
    while True:
        try:
            print(f"Username: {username}, Balance: {bank_acc[username]['balance']}")
            
            deposit_amount = float(input("Enter the amount to deposit: "))
            bank_acc[username]['balance'] += deposit_amount
            print("Deposit Successful!")
            print(f"New Balance: {bank_acc[username]['balance']}")
        except ValueError as e:
            print(e)

def main():
    while True:
        try:
            print("\n1. Create Account")
            print("2. Log In")
            print("3. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                create_acc()
            elif choice == 2:
                log_in()
                while True:
                    try:
                        print("\n1. Withdraw")
                        print("2. Deposit")
                        print("3. View Balance")
                        print("4. Exit")
                        choice = int(input("Enter ypur choice: "))
                      
                        if choice == 1:
                            withdraw(username)
                        if choice == 2:
                            deposit(username)
                        if choice == 3:
                            print(f"Username: {username}, Balance: {bank_acc[username]['balance']}")
                        if choice == 4:
                            print("Exiting....")
                        else:
                            print("Invalid Input")
                            break
                    except ValueError as e:
                            print (e)
            elif choice == 3:
                print("Exitingggggggg")
            else:
                print("Invalid choice. Please enter a number between 1 to 6")
        except ValueError:
            print ("Invalid input. Please enter a number")

main ()