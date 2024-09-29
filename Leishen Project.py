#Leishen Project

#Since may square root, gumamit ako library function ng python, so:
import math

#dine, pinapa input ko yung altitude 
#float pina-input ko kasi baka may decimals
altitude = float(input("Enter Altitude(in feet): "))

#tas dine, pinapa input ko yung temperature
#float rin pina input ko here if sakaling may decimals
temperature = float(input("Enter temperature(in Farenheit): "))

#tas nagawa ako ng mga conditions

#here, if negative daw yung altitude, which mean less than zero so: 
if altitude < 0:
    print ("Error")
    
#here, if altitude exceeds 36,000 feet daw, so more than 360000:
elif altitude > 36000:
    print ("Error")
    
#then here, if yung temperature is below zero, error din
elif temperature < 0:
    print ("Error")

#lastly, if wala daw error, solve gamit yung formula
#yung "math.sqrt" is yung library na inimport ko kanina sa unahan para magamit yung square root 
#yung "f" sa print is para ma call yung variable sa loob with the string na gusto mo which is "The computed airspeed"
#tas yung ".2f" is para 2 decimal places(yun sabi sa given)
else: 
    airspeed = math.sqrt((7 * altitude * temperature) / 2)
    print (f"The computerd airspeed is {airspeed:.2f}")