"""
This exercise acts relatively similar to the last one, except data will be pulled from a JSON file
This program will be able to read and write to the JSON file

"""
import json

def get_file(f: str):
    with open(f, 'r') as file:
        temp_d = json.load(file)
    return temp_d

def save_file(f: str, d: dict):
    with open(f, 'w') as file:
        json.dump(d, file)
    return

def add_names(d: dict):
    name = input("Please enter the name of the person you would like to add: ")
    birthdate = input(f"Please enter {name}'s birthdate in MM/DD/YYYY format: ")
    return d.update({name: birthdate})

def learn_dates(d: dict):
    print("\nPlease enter a name from the list below: \n")
    for i in d:
        print(i)
    s = input("\n")
    if s in d:
        print(f"\n{s}'s birthdate is {d[s]}.")
    else:
        print(f"\nSorry, {s} is not a valid name.")
    return
            
def program_loop(d: dict):
    print("Would you like to learn someones birthday or add a new birthday?")
    ans = input("Please enter learn or add: ")
    if 'd' in ans:
        d = add_names(d)
    else:
        learn_dates(d)
    ans = input("\nWould you like to do anything else?\nPlease enter yes or no: ")
    if 'n' in ans:
        return False

if __name__ == "__main__":
    file_name = "birthdays.json"
    birthday_dictionary = get_file(file_name)
    loop = True
    print("\nWelcome to the birthday dictionary!")
    while loop == True:
        loop = program_loop(birthday_dictionary)
    save_file(file_name, birthday_dictionary)