#For the third exercise in the brithdays project, we will print out how many birthdays are in each month from the JSON
import json
from collections import Counter

def read_file(f: str):
    with open(f, 'r') as file:
        data = json.load(file)
    return data

def month_num_to_name(d: dict):
    months = ["January", "Febuary", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
    temp_l = list()
    for i in d:
        month = (int(d[i][:2])) #returns only the first two characters of the value string and turns it into an int ('05' -> 5)
        temp_l.append(months[month - 1]) #adds the month name to the list
    return temp_l

if __name__ == "__main__":
    file_name = "birthdays.json"
    bday_dict = read_file(file_name)
    month_list = month_num_to_name(bday_dict)
    print(Counter(month_list)) #counts how many times each month is found then prints dict of values