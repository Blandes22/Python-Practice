#checks if any given string is a palindrome

str = input("Please enter a string: ")

#str[::-1] returns the string in reverse
if str == str[::-1]:
    print("Your string is a palindrome.")
else:
    print("Your string is not a palindrome.")