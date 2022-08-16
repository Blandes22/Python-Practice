#prints a list of all divisors from a user given number

n = int(input("Please enter a number: "))

''' 
range(1, n // 2 + 1) used because numbers cannot evenly divide into
numbers larger than half their value 

'''

l = [x for x in range(1, n // 2 + 1) if n % x == 0]
l.append(n)             #adds the number itself to the list of divisors            
print(l)