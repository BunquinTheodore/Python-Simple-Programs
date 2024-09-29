#Maalihan, Leishen Meryl 

list_of_resistors = []
valid_characters = ["1","2","3","4","5","6","7","8","9","."]

def main():
    while True:
        try:
            print ("-------------------------------------------")
            print ("Resistor Manager and Total Resistance Calculator")
            print ("1. Add Resistor")
            print ("2. Calculate Total Resistance")
            print ("3. Exit")
            print ("-------------------------------------------")
            choice = int(input("Enter choice: "))
            print ("-------------------------------------------")
            if choice == 1:
                add_resistor()
            elif choice == 2:
                calculate_total_resistance()
            elif choice == 3:
                print ("Exiting Program...")
                print ("-------------------------------------------")
                break
            else:
                print (f"Invalid Input: {choice}")
        except ValueError as e:
            print (f"Error occured: {e}")
            print ("-------------------------------------------")
            main()

def add_resistor():
    print ("Welcome to Add Resistor!")
    resistance_value = input("Enter Resistance Value: ")
    if all (char in valid_characters for char in resistance_value):
        list_of_resistors.append(float(resistance_value))
        print ("Successfully added resistance value!")
    else: 
        print (f"Invalid Input: {resistance_value}")
    

def calculate_total_resistance():
    if not list_of_resistors:
        print ("No resistors have been added yet...")
        return
    else:
        try: 
            print ("Choose Connection Type!")
            print ("1. Series Connection")
            print ("2. Parallel Connection")
            choice = int(input("Enter choice: "))
            if choice == 1:
                total_resistance = sum(list_of_resistors)
                print (f"Total Resistance: {total_resistance:.2f}")
            elif choice == 2: 
                for resistances in list_of_resistors:
                    reciprocals = 1/resistances
                    sum_of_reciprocals = 0
                    sum_of_reciprocals += reciprocals
                    total_resistance = 1/sum_of_reciprocals
                print (f"Total Resistance: {total_resistance:.2f}")
            else:
                print (f"Invalid Input: {choice}")
        except ValueError as e:
            print (f"Error Occured: {e}")

main()

                