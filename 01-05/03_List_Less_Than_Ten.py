#Asks user for a number then prints the list with all numbers lower than their number

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
n = int(input("Please enter a number: "))
b= [i for i in a if i < n]
print(b)