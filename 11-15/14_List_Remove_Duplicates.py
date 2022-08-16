#generates a random list and prints a new list without any duplicates

def rand_list():
    from random import randint
    return [randint(0,43) for i in range(1, randint(25,30))]

a = sorted(rand_list())
b = list(set(a))

print(a) #list with duplicates
print(b) #list without duplicates