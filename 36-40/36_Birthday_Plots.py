#For the final exercise of the birthdays project, we will parse the months as in exercise 35 then plot the data using bokeh

import json
from typing import Counter
import bokeh.plotting

def read_file(f: str):
    with open(f, 'r') as file:
        data = json.load(file)
    return data

def month_num_to_name(d: dict, m: list):
    temp_l = list()
    for i in d:
        month = (int(d[i][:2])) #returns only the first two characters of the value string and turns it into an int ('05' -> 5)
        temp_l.append(m[month - 1]) #adds the month name to the list
    return temp_l

if __name__ == "__main__":
    months = ["January", "Febuary", "March", "April", "May", "June", 
             "July", "August", "September", "October", "November", "December"] #months will be used for x-categories
    FILE_NAME = "birthdays.json"
    temp = read_file(FILE_NAME)
    birth_months = Counter(month_num_to_name(temp, months))
    x, y = list(zip(*birth_months.items()))                                    #separates the counted months 
    
    plot = bokeh.plotting.figure(x_range=months, title="Birthday Bokeh Plot") #gives plot a title and a the x axis a range of values
    plot.xaxis.major_label_orientation = 3.14/4                               #orients the x axis category names based on PI
    plot.vbar(x=x, top=y)                                                     #gives the plot values, where x is x axis and top is y axis
    
    bokeh.plotting.show(plot)                                                 #opens html file through web browser