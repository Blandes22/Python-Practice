"""
This exercise asks for the following code to be refactored into a function

    print(" --- --- ---")
    print("|   |   |   |")
    print(" --- --- ---")
    print("|   |   |   |")
    print(" --- --- ---")
    print("|   |   |   |")
    print(" --- --- ---")

There will be two functions, one for the original code and one for the new code
both functions will run and print their results to the console showing
"""

def old_func():
    print(" --- --- ---")
    print("|   |   |   |")
    print(" --- --- ---")
    print("|   |   |   |") 
    print(" --- --- ---")
    print("|   |   |   |")
    print(" --- --- ---")

def new_func():
    MATRIX_SIZE = 3                     #This variable allows for any size of board matrix to be created
    divider = " ---" * MATRIX_SIZE
    row = "|   " * (MATRIX_SIZE + 1)     #creates variables for neater code inside the for loop
    for i in range(MATRIX_SIZE):
        if i == 0:
            print(divider)               #ensures that there is a top to the board matrix
        print(row, divider, sep='\n')   

if __name__ =="__main__":
    print("Old function:\n")
    old_func()
    print("\nNew function:\n")
    new_func()