#Asks user for a number then tells them if it is odd or even. if it is a multiple of 4 it will tell them that instead.


i = int(input("Please enter a number: "))
if i % 4 == 0:
    print("Your number is a multiple of 4")
elif i % 2 == 0:
    print("Your number is even")
else: 
    print("Your number is odd")

#asks user for two numbers and checks if they divide evenly into each other
num = int(input("Please enter another number: "))
check = int(input("Please enter a non zero number to divide it by: "))

if num % check == 0:
    print("{} divides into evenly into {}".format(check, num))
else: 
    print("{} does not divide evenly into {}".format(check, num))