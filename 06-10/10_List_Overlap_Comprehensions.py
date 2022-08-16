#generates two random list of ints and prints a new list with only the elements in both lists

def generate_list():
    from random import randint
    return [randint(0, 20) for i in range(1, randint(15, 20))]

a = generate_list()
b = generate_list()
c = list(set([i for i in a if i in b]))
print(c)

#due to following the extra steps in project 05, this project is nearly identical to project 05