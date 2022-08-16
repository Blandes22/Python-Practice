#generates a random list and prints a new list with only the first and last elements


def list_ends(l: list):
    return [l[0], l[len(l) - 1]]

def generate_list():
    from random import randint
    return [randint(0,100) for i in range(1,randint(25,30))]

a = generate_list()
b = list_ends(a)
print(a) #full list
print(b) #only the start and end of the list