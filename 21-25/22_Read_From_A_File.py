"""
in this exercise, A file containing a large number of picture locations will be used
locations formated like so: /a/abbey/sun_aqswjsnjlrfzzhiz.jpg
we will need to find how many picutures are in each category ('abbey' is the category for the above example)

1. gather text from file
2. create dictionary to keep track of category:occurences (key:value)
3. iterate through data and check if category is in the dictionary
4. if category is in the dictionary, add 1 to current value
5. if category is not in the dictionary, create new dictionary element and set value to 1
"""

def collect_data(s: str):
    open_file = open(s, 'r')
    text = open_file.read()
    open_file.close()
    
    return text

def count_data(s: str):
    temp = s.split('\n')
    data = dict()
    for i in temp:
        j = i.split('/')
        temp_s = '/'.join(j[2:(len(j) - 1)])

        if temp_s in data:
            data[temp_s] += 1
        else:    
            data[temp_s] = 1
    
    return data

if __name__ == "__main__":
    file_name = "Training_01.txt"
    data = collect_data(file_name)
    counted_categories = count_data(data)
   
    for k, v in counted_categories.items():
        print(f"{k} : {v}")