"""
take two files and find what numbers are in both files
read both files to lists
use list comp to find only the numbers that are the same
print results to screen

"""

def file_to_list(s: str):
    with open(s, 'r') as file:
        return (file.read()).split('\n')

def list_overlap(l1: list, l2: list):
    return [i for i in l1 if i in l2]

if __name__ == "__main__":
    happy_num = file_to_list("happynumbers.txt")
    prime_num = file_to_list("primenumbers.txt")
    overlap = list_overlap(happy_num, prime_num)

    print(overlap)