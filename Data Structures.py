#DATA STRUCTURE COLLECTIONS

#one.append(5)
#two = list(one)
#two.remove(1)
#one = two 
#print (one)
#two = list(one)
#two[1] = -1
#print (two)

lost = {1,2,3,4,1,2,3,4}
#lost.insert(3,3.5)
print (lost)

#two = {1,2,3,4,5}
#three = list(two)
#print (type(three))

#four = {1,2,3,4}
#print (four[-2])

#five = {"one" : 1, "two": 2, "three": 3}
#six = {"four": 4, "Five" : 5, "Six": 6}
#five.update(six)
#print (five)
#five ["one and decimal"] = 1.1111
#print (five)
#print (five["one"])
#s = five.get("two")
#print (s)

#q = five.keys()
#w = five.values()
#print (f"{q} : {w}")


#six = {1,2,3,4, 5}
#six.add(7)
#print (six)
#print (six[2:5])
#seven = {3,5,6,5}
#print (3 in seven)

game_library = {
    "Mobie Legends" : {"Load" : 20, "Quantity" : 10},
    "Call of Duty" : {"Load": 30, "Quantity" : 5},
    "Naturo Shippuden" : {"Load" : 40, "Quantity" : 8}
}

while True: 
    for game, info in game_library.items():
        print(f"{game} -  Load: {info['Load']}, Quantity:{info['Quantity']}")
    break