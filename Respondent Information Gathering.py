#Respondent Information Gathering

def thefullname ():
    firstname = list((input("Enter your first name: ")))
    middlename = list ( (input("Enter middle name: ")))
    lastname = list((input("Enter last name: ")))
    fullname = list (zip(firstname, middlename, lastname))
    print (fullname)
    return fullname

thefullname()