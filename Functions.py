# Add 1 to a and store it in B

def add1(a):
    """
    This function takes as parameter a number and add one
    """


    B = a+1
    print(a," if you add one will be: ",B)

add1(5)
print(help(add1))

print("*"*100)

# Lets declare a function that multiplies two numbers

def mult(a,b):

    C = a*b

    return C
    print("This wont be printed")


Result = mult(12,2)
print(Result)
print("*"*100)

# Lets sen string as a paramenter to our multiplication function

Result = mult(5, " Hello World ")
print(Result)
print("*"*100)

# Function definition

def square(a):

    """

    Square the input and add 1
    """
    b = 1

    c = a*a+b
    print(a, " If you square +1 ", c)


z = square(2)
print("*"*100)

# Firs block
A1 = 4
B1 = 5
C1 = A1*B1+2*A1*B1-1
if (C1 < 0):
    C1 = 0
else:
    C1 = 5

print(C1)

print("*"*100)

# Firs block
A1 = 0
B1 = 0
C1 = A1*B1+2*A1*B1-1
if (C1 < 0):
    C1 = 0
else:
    C1 = 5
print(C1)

print("*"*100)

# Make a function for the calculation above

def equation(A1,B1):

    C1 = A1 * B1 + 2 * A1 * B1 - 1
    if (C1 < 0):
        C1 = 0
    else:
        C1 = 5

    return C1


C2 = equation(4,5)
C3 = equation(0,0)
print(C2)
print(C3)

print("*"*100)

# Example for setting a parameter with default value

def isGoodRaiting(rating = 4):

    if(rating < 7):
        print("This album sucks it's raiting is: ", rating)

    else:
        print("This album is good it's raiting is: ", rating)


isGoodRaiting(1)
isGoodRaiting(10)
isGoodRaiting()
print("*"*100)

# Lets create a function with packed arguments

def printAll(*args):


    print("Num of arguments: ", len(args))

    for argument in args:
        print(argument)

printAll("Red", "Yellow", "Blue", "Orange")
print("*"*100)

printAll("Red", "Yellow")
print("*"*100)

# Kwargs parameter

def printDictionary(**kwargs):

    for key in kwargs:

        print(key + ": " + kwargs[key])
printDictionary(Country = 'Canada', Providence = 'Ontario', City = 'Toronto')
print("*"*100)


# Funtion
def addItems(list):

    list.append("Three")
    list.append("Four")

My_list = ["One", "Two"]

print(My_list)

addItems(My_list)
print(My_list)


print("*"*100)

#Example of a global variable

Artist = "Michael Jackson"

def printer1(artist):

    global internal_var
    internal_var = "Elvis"
    print(artist," is an artist")

printer1(Artist)
printer1(internal_var)







