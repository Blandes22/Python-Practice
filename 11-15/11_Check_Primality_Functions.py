def is_prime(n: int):
    if (n == 2) or (n == 3):
        return True
    if (n % 2 == 0) or (n % 3 == 0):
        return False
    #above checks values 2 and 3 and if numbers are divisble by 2 or 3
    #if both checks above fail, below checks all other values up  to the sqrt(n)
    for i in range(5, int(n ** 0.5) + 1, 2): 
        if n % i == 0:
            return False
    
    return True

num = int(input("Please enter a number to check its primality: "))

if is_prime(num):
    print("{} is a prime number".format(num))
else:
    print("{} is not a prime number".format(num))