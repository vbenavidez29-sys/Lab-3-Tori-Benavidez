# this function adds two numbers 
def add(x,y):
    print(x + y)

add(6,7)
# this function subtracts two numbers 
def sub(x,y):
    print(x - y)

add(6,7)

# this function multiplies two numbers 
def mul(x,y):
    print(x*y)

add(6,7)
# this function divides two numbers 
def div(x,y):
    print(x/y)

################################################################
#################################################################
###Start of program
print("Welcome to my awsome calulator")
print("What would you like to do?")
print("Type (a)dd (s)ubtract (m)ultiply (d)ivde (q)uit)")

x= int(input("Enter your first number: "))
y= int(input("Enter your our second number: "))

add(x,y)
sub(x,y)
div(x,y)
mul(x,y)