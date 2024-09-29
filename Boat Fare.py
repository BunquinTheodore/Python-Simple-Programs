#Boat Fare

Name = str(input("Enter name: "))
Age = int(input ("Enter age: "))

if Age >= 18:
    fare = 500
elif Age < 18 and Age > 10:
    fare = 450
else:
    fare = 400
    
print (f'"Hello {Name}, you are {Age} years old and you fare is {fare}"')
    
