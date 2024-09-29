#Create a program that accepts an array size, and input as many elements in the unordered array depending on the input size. 
# Print list from minimum to maximum.

#Enter index 0:
# Enter index 1:
# etc.

# The list is: [1, 34, 32, 344, 223, 2, -1]
# The ordered list is: 

def generateList(size, array):
    for i in range(0, size):
        temp = int(input("Enter index " + str(i) +":"))
        array.append(temp)
        
    print("The list is:", array)
        
my_list = []
list_size = int(input("Enter the list size: "))

generateList(list_size, my_list)

my_list.sort()
print("Ordered list:", my_list)
        

