#this program will take a number and find if its inside of a randomly generated list
#once the number is found or not found, the program will print true or false
def generate_sorted_list():
    from random import randint
    l = ([randint(1, 999) for i in range(1, 600)])
    l.sort()
    return l

def binary_search(key: int, low: int, high: int, l: list):
    """
    binary search finds the middle index 
    mid = ((lowest index + highest index) / 2)
    checks if middle index is ==, <, or > than the key
    if key == mid, return true
    if key > mid, return the function and check the right side of the list
    if key < mid, return the function and check the left side of the list

    if low == mid return false 
    
    """
    mid = (low + high) // 2

    if l[mid] == key:
        return True
    if (low == mid) or (high == mid) and (l[mid] != key):
        return False
    if key > l[mid]:
        return binary_search(key, mid, high, l)
    if key < l[mid]:
        return binary_search(key, low, mid, l)

if __name__ == "__main__":
    l = generate_sorted_list()
    key = int(input("Please enter a number between 1 and 999 to search for in the list: "))
    print(binary_search(key, 0, len(l) + 1, l))