#BSU Portal 

student_account = {}



def main():
    while True: 
        print ("Welcome to Batangas State Alangilan Portal\n")
        print ("1. Sign-Up For Student Account")
        print ("2. Sign-In For Student Account")
        print ("3. Exit Portal")
        choice = int(input("Enter choice of action: "))
        try: 
            if choice == 1:
                sr_code = input("Enter SR-Code: ")
                password = input("Enter password: ")
                sign_up(sr_code, password)
            elif choice == 2:
                sign_in()
            elif choice == 3:
                exit_portal
            else:
                print ("Invalid Input")
                break
        except ValueError as e:
            print (f"Error: {e}")
    
    
def sign_up(sr_code, password):
    if sr_code in student_account:
        print ("SR-Code is already used  by another student!\n1")
    else:
        student_account[sr_code] = {"password" : password}
        print ("Sign-up for student account done successfully!\n")
        return
    
def sign_in():
    pass

def exit_portal():
    pass

main()