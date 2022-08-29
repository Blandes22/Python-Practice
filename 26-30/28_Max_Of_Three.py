"""
This exercise will require a function to find the max of 3 variables without using the max() function

"""

def find_max(x: int, y: int, z: int):
    nums = [x, y, z]
    current_max = x
    for i in nums:
        if i > current_max:
            current_max = i
    return current_max



if __name__ == "__main__":
    print(find_max(946, 745, 1000))