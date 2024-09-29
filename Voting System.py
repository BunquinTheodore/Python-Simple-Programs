#Voting System 

name = str(input("Enter your name: "))
age = int(input("Enter your age: "))

if age >= 18:
    print (f"{name}, you can vote!")
else:
    print (f"Sorry {name}, you cannot vote yet:()")
    