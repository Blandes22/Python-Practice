"""
def reverse_list(l: list):
    return l[::-1]

a = str.split()                              1. makes the string into a list
a = reverse_list(a)                          2. custom function that returns the string in reverse order (see line two)
a = " ".join(a)                              3. makes the list into a string with spaces between each element

a = " ".join(reverse_list(str.split()))      can also be written in one line (3(2(1)))
"""

"""
instead of having a seperate function to reverse the list, its best to have
a function that will instead, return a reversed string. Alot of code above 
will not be changed for this

a = str.split()                1. used to turn the list into a string              
a = a[::-1]                    2. used to reverse the order of the list elements
a = " ".join(a)                3. used to join the list elements into a string with spaces between each element

"""

def reverse_string(s: str):
    return " ".join(str.split()[::-1])

str = "this is a list and it is going to be reversed"
print(reverse_string(str))