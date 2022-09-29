def towers_of_hanoi(n: int, f: list, a: list, t: list):
    # f == X, a == Y, t == Z
    
    #base case of n == 1
    if n == 1:
        t.append(f.pop())
        print('-' * 15, from_tower, aux_tower, to_tower, sep='\n')
        return
    
    #move n-1 disks from X to Y using Z as the auxiliary
    towers_of_hanoi(n-1, f, t, a)
    
    #move remaining disk from X to Z
    t.append(f.pop())
    print('-' * 15, from_tower, aux_tower, to_tower, sep='\n')
    #move n-1 disks from Y to Z using X an the auxiliary 
    towers_of_hanoi(n-1, a, f, t)

if __name__ == "__main__":
    DISKS = 3
    from_tower = [(DISKS - i) for i in range(DISKS)]
    to_tower = list()
    aux_tower = list()
    print(from_tower, aux_tower, to_tower, sep='\n')
    towers_of_hanoi(DISKS, from_tower, aux_tower, to_tower) 