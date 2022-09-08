#Asks user for name and age and prints a message using an f string


name = input("Please enter your name: ")
age = input("Please enter your age: ")
year = 100 - int(age) + 2022
message = f"{name}, in the year {year}, you will be 100 years old."

print(message)