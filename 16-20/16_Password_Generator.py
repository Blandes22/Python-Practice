#asks user how strong of a password they want then prints a random password
#if strong, password will be 12 characters long with at least one of each category
#if weak, a adjective and a noun will be picked at random followed by 2 numbers
import random
import string

#collection of elements used for password making
noun = "Time Person Year Way Day Thing Man World Life Land Part Child Eye Woman Place Work Week Case Point Dog Cat Number Group Problem Fact".split()
adjective = "good new first last long great little own other old right big high odd small large next early young eager few public bad same able".split()
digit = string.digits
lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
symbol = string.punctuation
all = digit + lower_case + upper_case + symbol

ans = input("For a weak password type weak, for a strong password type strong: ").lower()

if 's' in ans:
    #guarentees that one character from each type will be in the password then adds the remaining characters
    temp = (random.choice(digit) + random.choice(lower_case) + random.choice(upper_case) + random.choice(symbol))
    for i in range (12 - 4): #used for a 12 digit password minus the four from above
        temp += random.choice(all)   

    temp = [x for x in temp] #list needed for shuffle function
    random.shuffle(temp)     
    password = "".join(temp)

    print(f"Your new password is: \n{password}")

else:
    temp = random.choice(adjective) + random.choice(noun) + str("".join(random.sample(digit, 2)))
    password = "".join(temp)

    print(f"Your new password is: \n{password}")
