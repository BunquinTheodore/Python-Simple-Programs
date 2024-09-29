operation = input ("Enter an operator: + , -, / , * :  ")
num1 = int (input("Enter 1st number: "))
num2 = int (input("Enter 2nd number: "))

if operation == "+":
    result = num1 + num2 
    print (int(result))
elif operation == "-":
    result = num1 - num2
    print (int(result))
elif operation == "/":
    if num2 == 0: 
        print ("Cannot divide by 0")
        breakpoint
    else:
        result = num1 / num2
        print (int(result))
elif operation == "*": 
    result = num1 * num2
    print (int (result))
elif operation not in  ("+", "-", "/", "*"):
    print (f"Invalid operator: {operation}")
else:
    print ("An error occured")