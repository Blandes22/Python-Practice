"""
This exercise takes the code from exercise 1 and generalize it with the datetime library
"""

import datetime

date = datetime.datetime.now()
name = input("Please enter your name: ")
age = input("Please enter your age: ")
year = 100 - int(age) + date.year
message = f"{name}, in the year {year}, you will be 100 years old."

print(message)