# Given a self.matrix of size 'n' (self.matrix_size = n) filled with 0's and 1's find the largest region of connected 1's.
# a 1 will be connected with another 1 if it occupies any of the 8 spaces next to it (up/down, left,right, and diaganols)
# randint used to generate self.matrix
from random import randint

class ConnectedCells:
    def __init__(self):
        self.matrix_size = 4
        self.matrix = [[randint(0,1) for i in range(self.matrix_size)] for i in range(self.matrix_size)]
        self.r = 0                      # row
        self.c = 0                      # column
        self.memo = list()              # used to keep track of which coordinate pairs have been checked
        self.largest_region = 0         # will be saved as the largest region    
        self.cur_region = 0             # will be used to keep track of the current region size

    def iterate_cells(self):
        self.memo.append([self.r, self.c])
        # check if coordinate is 1, if so use get_region to find how many 1s are connected
        if self.matrix[self.r][self.c] == 1:
            self.cur_region = 0
            self.get_region(self.r, self.c)      
        # update r(row) and c(col) until they are return a value that has not already been checked
        while [self.r, self.c] in self.memo:
            self.c += 1
            #makes sure that the value of c(col) 
            if self.c > (self.matrix_size-1):
                self.c = 0
                self.r += 1
            if self.r > (self.matrix_size-1):
                return  #return if r is above self.matrix_size, r can only go above if c can go above
        self.iterate_cells()
    
    def get_region(self, r, c):
        self.cur_region += 1
        #create list of all 8 new directions and iterate through them to check values
        directions = [[r-1, c-1], [r-1, c], [r-1, c+1], [r, c-1], 
                      [r, c+1], [r+1, c-1], [r+1, c], [r+1, c+1]]
        for i in directions:
            #prevent any error values (i.e [-1, -1], [self.matrix_size, self.matrix_size])
            if ((i[0] not in range(self.matrix_size)) or
                (i[1] not in range(self.matrix_size))):
                continue
            #set new temp values for r(row) and c(col) used to find new self.matrix value and for the get_region function
            temp_r = i[0]
            temp_c = i[1]
            if (i not in self.memo) and (self.matrix[temp_r][temp_c] == 1):
                #update memo to prevent this pair from being called again
                self.memo.append(i)
                self.get_region(temp_r, temp_c)
            #update largest region value if needed    
            if self.cur_region > self.largest_region:
                self.largest_region = self.cur_region
    
    def print_matrix(self):
        for i in self.matrix:
            print(i)

def main():
    sol = ConnectedCells()
    sol.print_matrix()
    sol.iterate_cells()
    print(f"Largest region of 1's: {sol.largest_region}")

if __name__ == "__main__":
    main()