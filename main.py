EASTER_EGG_NUMBER = 18

# this function adds two numbers 
def add(x,y):
    if x == EASTER_EGG_NUMBER or y == EASTER_EGG_NUMBER:
        print("Easter egg unlocked! 18 is the magic number!")
    print(x + y)
# this function subtracts two numbers 
def sub(x,y):
    if x == EASTER_EGG_NUMBER or y == EASTER_EGG_NUMBER:
        print("Easter egg unlocked! 18 is the magic number!")
    print(x - y)
# this function multiplies two numbers 
def mul(x,y):
    if x == EASTER_EGG_NUMBER or y == EASTER_EGG_NUMBER:
        print("Easter egg unlocked! 18 is the magic number!")
    print(x*y)
# this function divides two numbers 
def div(x,y):
    if x == EASTER_EGG_NUMBER or y == EASTER_EGG_NUMBER:
        print("Easter egg unlocked! 18 is the magic number!")
    print(x/y)

#################################################################
###Start of program
if __name__ == "__main__":
    print("Welcome to my awsome calulator")

    while (True):
        print("What would you like to do?")
        print("Type (a)dd (s)ubtract (m)ultiply (d)ivde (q)uit)")

        user_choice=input(": ")
    #print(user_choice)
    
        if user_choice == 'a' : 
            x= int(input("Enter the first number: "))
            y= int(input("Enter the first number: "))
            add(x,y)

    # elif for subtract
        elif user_choice == 's' : 
            x= int(input("Enter the first number: "))
            y= int(input("Enter the first number: "))
            sub(x,y)

    # elif for multiply 
        elif user_choice == 'm' : 
            x= int(input("Enter the first number: "))
            y= int(input("Enter the first number: "))
            mul(x,y)

    # elif for divide 
        elif user_choice == 'd' : 
            x= int(input("Enter the first number: "))
            y= int(input("Enter the first number: "))
            div(x,y)

        elif user_choice == 'q':
            print("Thanks for using my awesome calc app!!")
            break

        else:
            print("Invalid input. Please try again.")

    # elif for quit 
    # break- this will not work without a loop 

    # else - does not need a condition 
    # else : 
    # print invaild input you dum dum 
