#BUILDING PROGRAM 2 
user_database = {}

def sign_up():
    print ("Signing Up you Account")
    while True:
        try:
            username = str(input("Enter your username: "))
            if username in user_database:
                print (f"{username} is in database already, input another one")
                continue
            password = str(input("Create your password: "))
            email = str (input("Enter email: "))
            user_database [username] = {"password" : password, "email" : email} 
            print ("You have successfully signed up")
            exit = input("Enter 1 to exit")
            if exit == 1:
                return
        except (ValueError,IndexError) as e:
            print (f"Error occured:{e}")
            break
        
def sign_in():
    print("Sign in your Account")
    while True:
        try:
            temporary_name_holder = str(input("Enter your username: "))
            if temporary_name_holder in user_database:
                continue
            if temporary_name_holder not in user_database:
                print ("Username not found in database")
                return
            temporary_password_holder = str (input("Enter you password: "))
            temporary_email_holder = str (input("Enter your email: "))
            if temporary_name_holder == user_database["username"] and temporary_password_holder == user_database["password"]:
                print ("Correct Username/Password!")
            else:
                print ("Incorrect username/password")
            if temporary_email_holder == user_database["email"]:
                print ("Email is valid")
            else:
                print ("Invalid email")
            break 
        except (ValueError, IndexError) as e:
            print (f"Error occured: {e}")
        return
    
def edit_data():
    print ("Editing Data")
    print ("Current Database: ")
    if not user_database:
        print ("Database is empty")
    else: 
        print (f"Username: {user_database["username"]}\nPassword: {user_database["password"]}\nEmail: {user_database['email']}")
    while True:
        try:
            print ("1. Edit username")
            print ("2. Edit Password")
            print ("3. Edit Email")
            choice = ("\n Enter number within scope (1,2,3)")
            if choice == 1:
                tem_name = input ("Enter your current username: ")
                if tem_name not in user_database:
                    print ("Username not in data base")
                    return
                else:
                    new_name = input ("Enter New Username: ")
                    user_database["email"] = new_name
                    print ("Successfully Edited!")
            if choice == 2:
                tem_pass = input ("Enter current password: ")
                if tem_pass not in user_database:
                    print ("Password not in database")
                else:
                    new_pass = input ("Enter New Password: ")
                    user_database ["password"] = new_pass
                    print ("Successfully Edited!")
            if choice == 3:
                tem_email = input ("Enter current email: ")
                if tem_email not in user_database:
                    print ("Email not in database")
                else:
                    new_email = input ("Enter New Email: ")
                    user_database ["email"] = new_email
                    print ("Successfully Edited!")
                    return
                    
        except (ValueError, IndexError) as e:
            print (f"Error occured:{e}")
            break

    
def delete_user():
    print ("Delete Username")
    while True:
        try:
            delete_username = input("Enter the username to be deleted: ")
            if delete_username not in user_database: 
                print ("Username not in database")
            else: 
                del user_database["username"]
                break
        except (ValueError, IndexError) as e:
            print (f"Error Occured: {e}")
    print ("Username Deleted")
    return
    
def view_database():
    print ("Viewing Database")
    if not user_database:
        print ("Userdatabase is Empty")
    else:
        print (f"Username: {user_database["username"]} \n Password: {user_database["password"]}\n Email: {user_database['email']}")
    print ("Viewing Database is Complete")
    exit = input("Enter '1' to exit")
    if exit == 1:
        return
    
def search_user():
    print ("Search Username \n")
    search_name = input ("Enter the username to be searched: ")
    if search_name in user_database:
        print ("Username Found!\n")
        print (user_database)
    else: 
        print ("Not Matching Username")
        return
    
def change_password():
    print ("Changing Password")
    while True:
        try:
            sign_username = input ("Enter usernanme to change password: ")
            if sign_username not in user_database:
                print ("Username not found, try again")
                return
            else: 
                new_pass = input ("Enter New Password: ")
                user_database["password"] = new_pass
                print ("Password Changed Successfully")
                return
        except (ValueError, IndentationError, IndexError) as e:
            print (f"Error occured: {e}")
            break
      
def main():
    try: 
        print ("Main Menu")

        print ("1. Sign Up")
        print ("2. Sign In")
        print ("3. Edit Data")
        print ("4. Delete User")
        print ("5. View Database")
        print ("6. Search User")
        print ("7. Change Password")
        print ("8. Exit Menu")
    
        choice = int(input("Enter a number of your choice from 1 - 10: "))
    
        if choice == 1:
            sign_up()
        elif choice == 2:
            sign_in()
        elif choice == 3:
            edit_data()
        elif choice == 4:
            delete_user()
        elif choice == 5:
            view_database()
        elif choice == 6:
            search_user()
        elif choice == 7:
            change_password()
        elif choice == 8:
            print ("Exiting Program")
            return
        else:
            print ("Enter a number within choices")

    except ValueError as e:
        print (e)
    
main()
    