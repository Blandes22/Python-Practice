#Asks user for name and age and prints a message to the console telling them what year they will turn 100 in


name = input("Please enter your name: ")
age = input("Please enter your age: ")
year = 100 - int(age) + 2022
message = "{}, in the year {}, you will be 100 years old.".format(name, year)

print(message)


#Asks user to enter a number then prints the previous message that many times
n = int(input("Please enter a second number: "))
print(message * n)