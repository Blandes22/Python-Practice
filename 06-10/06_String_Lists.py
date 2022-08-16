#checks if any given string is a palindrome

str = input("Please enter a string: ")

if str == str[::-1]:
    print("Your string is a palindrome.")
else:
    print("Your string is not a palindrome.")