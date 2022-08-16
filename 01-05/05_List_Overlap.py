#creates two random lists and prints a new list with only their duplicates

def rand_list():
    from random import randint
    return [randint(0,43) for i in range(1, randint(25,30))]
    
a = rand_list()
b = rand_list()
c = list(set([i for i in a if i in b]))
print(c)

#due to following the extra steps in this project, this project is nearly identical to project 10