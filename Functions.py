#PRACTICING FUNCTIONS 

#def add (num1 , num2):
#    result = num1 + num2 
 #   return result
 
 #OR
 
#def add (num1, num2):
  #   result = num1 + num2
  #   return result 

#phone = add (150, 200)
#print (phone)

#def add (a, b= 10):
   # c = a + b
   # return c

#d = add(1, 2)
#print (d)

#PRINTING WITHIN FUNCTION
#def a ():
    #b = 1
   # print (b)
    
#a()

#CALLBACK FUNCTIONS
#def square (x):
 #   a = x*x
  #  return a

#def cube (x):
 #   b = x*x*x
  #  return b

#def apply (func, x):
 #   return func(x)

#a = apply(square,2)
#b = apply(cube, 2)

#print (a) 
#print (b)

#ARGS AND KWARGS
#def addition (*numbers):
 #   return sum(numbers)

#a = addition (1,2,3,4,5,6)
#print (a)

#def sum_of_numbers(*summation):
  #total = 0
 # for numbers in summation:
  #  total = total + numbers
  #return total
  
#solve_this = sum_of_numbers(1,2,3)
#print (solve_this)

#def area (**kwargs):
 # width = kwargs.get("width", 5)
 # height = kwargs.get("height", 5)
 # the_area = width * height
  #return the_area

#rectangle = area( )
#print (rectangle )
  
#APPLYING MAP


#def square (x):
 # the_squre = x ** 2
  #return the_squre

#def cube (x):
 # the_cube = x ** 3
 # return the_cube

#def even(x):
 # even_numbers =  x % 2 == 0 
  #return even_numbers

#def odd (x):
 # odd_numbers = x % 2 != 0 
 # return odd_numbers
  
#numbers = (1,2,3,4,5)

#squares = list(map(square, numbers))
#cubes = list(map(cube, numbers))
#even_square_numbers = list(filter (even, squares))
#odd_square_numbers = list(filter (odd, squares))
#even_cube_numbers = list(filter (even, cubes))
#odd_cube_numbers = list(filter (odd, cubes))
#print (f"The squares are: {squares}")
#print (f"The cubes are: {cubes}")
#print (f"The even square numbers: {even_square_numbers}")
#print (f"The odd square numbers: {odd_square_numbers}")
#print (f"The even cube numbers: {even_cube_numbers}")
#print (f"The odd cube numbers: {odd_cube_numbers}")
#print (reduced)

#USING SORTED()
#words = ("dog", "cat", "mouse", "rat", "deer", "ant", "fly")
#numbers = [5,8,9,4,2,4,7,8,5,2]

#alpabehtically = sorted(words)
#counting = sorted(numbers)

#print (alpabehtically, counting)

#USING LAMBDA

#add = lambda x, y: x+y
#sum = add(1,2)
#print (sum)

#USING HIGHER FUNCTIONS

#def add(number):
  #return lambda result: result + number
  
#starting_number = add (8)
#result = starting_number (7)
#print (result)

#numbers = (1,2,3,4,5)
#squares = list(map (lambda result: result ** 2, numbers))
#even = list(filter (lambda result: result % 2 == 0, squares))

#for square in squares:
 # print (square)
#for even_numbers in even:
 # print (even_numbers)
 

