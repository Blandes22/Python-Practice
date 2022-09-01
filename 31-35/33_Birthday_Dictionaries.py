"""
This project holds a python dictionary of names and birthdates
the user will be asked to select a name from the list
once selected their birthdate will be shown
"""

if __name__ == "__main__":
    birthday_dictionary = {
        "Tracey Painter" : "05/16/1939",
        "Rocio Curtis" : "08/19/1977",
        "Ralph Isreal" : "04/22/1943",
        "Elaine Campos" : "11/14/1984",
        "Salvador Jones" : "01/30/1940"
    }

    print("Welcome to the birthday dictionary!\nPlease enter of the names below to learn their brithday.\n")
    for i in birthday_dictionary:
        print(i)
    s = input("\n")
    if s in birthday_dictionary:
        print(f"\n{s}'s birthdate is {birthday_dictionary[s]}.")
    else:
        print(f"\nSorry, {s} is not a valid name.")