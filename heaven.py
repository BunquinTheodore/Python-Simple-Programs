def physical_properties():
    print("PHYSICAL PROPERTIES")
    print("1. Viscosity")
    print("2. Turbidity")
    print("3. Electrical Conductivity")
    print("4. All")
    print("5. Back")
    choice = input("Enter your choice: ")

    if choice == "1":
        viscosity = float(input("Enter viscosity value (0.89 - 1.0): "))
        if 0.89 <= viscosity <= 1.0:
            print("Viscosity is within acceptable range.")
            return viscosity
        else:
            print("Viscosity is not within acceptable range.")
            return None
    elif choice == "2":
        turbidity = float(input("Enter turbidity value (1 - 5): "))
        if 1 <= turbidity <= 5:
            print("Turbidity is within acceptable range.")
            return turbidity
        else:
            print("Turbidity is not within acceptable range.")
            return None
    elif choice == "3":
        conductivity = float(input("Enter electrical conductivity value (50 - 1500): "))
        if 50 <= conductivity <= 1500:
            print("Electrical conductivity is within acceptable range.")
            return conductivity
        else:
            print("Electrical conductivity is not within acceptable range.")
            return None
    elif choice == "4":
        viscosity = float(input("Enter viscosity value (0.89 - 1.0): "))
        turbidity = float(input("Enter turbidity value (1 - 5): "))
        conductivity = float(input("Enter electrical conductivity value (50 - 1500): "))
        if 0.89 <= viscosity <= 1.0 and 1 <= turbidity <= 5 and 50 <= conductivity <= 1500:
            print("All physical properties are within acceptable ranges.")
            return viscosity, turbidity, conductivity
        else:
            print("One or more physical properties are not within acceptable ranges.")
            return None
    elif choice == "5":
        return None
    else:
        print("Invalid choice.")
        return None

def chemical_properties():
    print("CHEMICAL PROPERTIES")
    print("1. pH level")
    print("2. Chlorine")
    print("3. All")
    print("4. Back")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        ph_level = float(input("Enter pH level (6.5 - 8.5): "))
        if 6.5 <= ph_level <= 8.5:
            print("pH level is within acceptable range.")
            return ph_level
        else:
            print("pH level is not within acceptable range.")
            return None
    elif choice == "2":
        chlorine = float(input("Enter chlorine level (0.2 - 4.0): "))
        if 0.2 <= chlorine <= 4.0:
            print("Chlorine level is within acceptable range.")
            return chlorine
        else:
            print("Chlorine level is not within acceptable range.")
            return None
    elif choice == "3":
        ph_level = float(input("Enter pH level (6.5 - 8.5): "))
        chlorine = float(input("Enter chlorine level (0.2 - 4.0): "))
        if 6.5 <= ph_level <= 8.5 and 0.2 <= chlorine <= 4.0:
            print("All chemical properties are within acceptable ranges.")
            return ph_level, chlorine
        else:
            print("One or more chemical properties are not within acceptable ranges.")
            return None
    elif choice == "4":
        return None
    elif choice == "5":
        exit_program(None, None, None, None, None) 
    else:
        print("Invalid choice.")
        return None

def exit_program(viscosity, turbidity, conductivity, ph_level, chlorine):
    print("Exiting program. Analyzing water safety...")

    if (
        viscosity is not None
        and turbidity is not None
        and conductivity is not None
        and ph_level is not None
        and chlorine is not None
    ):
        if (
            0.89 <= viscosity <= 1.0
            and 1 <= turbidity <= 5
            and 50 <= conductivity <= 1500
            and 6.5 <= ph_level <= 8.5
            and 0.2 <= chlorine <= 4.0
        ):
            print("Water is safe for domestic use.")
        else:
            print("Water is not safe for domestic use.")
    else:
        print("Not all parameters are available for analysis.")

def main():
    print("Welcome to HydroSafe Water Analyzer")
    while True:
        print("------------------------------------")
        print("1. Choose Water Parameters")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            while True:
                print("------------------------------------")
                print("1. Physical Properties")
                print("2. Chemical Properties")
                print("3. Both")
                print("4. Back")
                sub_choice = input("Enter your choice: ")
                print("------------------------------------")

                if sub_choice == "1":
                    viscosity = physical_properties()
                elif sub_choice == "2":
                    ph_level = chemical_properties()
                elif sub_choice == "3":
                    viscosity = physical_properties()
                    turbidity, conductivity = chemical_properties()
                elif sub_choice == "4":
                    break
                else:
                    print("Invalid choice.")

                if sub_choice in ["1", "3"] and viscosity is None:
                    continue 
                elif sub_choice == "2" and ph_level is None:
                    continue  
                elif sub_choice == "3" and (turbidity is None or conductivity is None):
                    continue  
        elif choice == "2":
            exit_program(None, None, None, None, None)  
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
