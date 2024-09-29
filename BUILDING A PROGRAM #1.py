#BUILDING A PROGRAM
this_dict = {}

def create_acc():
    print ("Create Account")
    while True:
        try:
            this_dict["name"] = input("Enter username: ")
            this_dict["passkey"] = input ("Enter password: ")
        

        except ValueError as e: 
            print (e)
        
   
def sign_in():
    try: 
        temporary_name = input("Enter your name: ")
        temporary_password = input("Enter you password: ")
        if temporary_name == this_dict["name"] and temporary_password ==  this_dict["passskey"]:
            print ("Successfully Logged in!")
        elif temporary_name and temporary_password != this_dict["name"] and this_dict["passkey"]:
            print ("Wrong Confirmation, try again")
        else: 
            print ("You forgot your passsword, go back to menu!")
            main()
    except ValueError as e:
        print (e)
        
def change_password():
    try: 
        print ("Changing your password")
        new_passkey = input("Enter new password")
        this_dict["passkey"] = new_passkey
    except ValueError as e:
        print (e)
    
    
def main():
    print ("1. Create account")
    print ("2. Sign In")
    print ("3. Change Password")
    print ("4. Exit")
    
    choice = int(input("Enter a number of choice: "))
    if choice == 1:
        create_acc()
    elif choice == 2:
        sign_in()
    elif choice == 3:
        change_password()
    elif choice == 4:
        print ("End of Program")
    else: 
        print ("Invalid Input: ")
                
main()