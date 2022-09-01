#creates two random lists and prints a new list with only their duplicates

def rand_list():
    from random import randint
    return [randint(0,40) for i in range(1, randint(25,(30 + 1)))] #list of 25 to 30 ints ranging from 0 t 40
    
a = rand_list()
b = rand_list()
c = list(set([i for i in a if i in b])) #returns list for all value of a in b, then turns list into set to remove duplicates, and back to a list
print(c)

#due to following the extra steps in this project, this project is nearly identical to project 10