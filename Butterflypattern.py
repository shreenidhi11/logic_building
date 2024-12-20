N = 1
row = 2*N -1
cols = 2*N -1
display = 2
esc = row - display
mid = row 

for r in range(row+1):
    if r <= (row//2):
        for i in range(display//2):
            print("*", end=" ")
        # print(end=" ")
        # loop for escaping
        for i in range(esc):
            print(" ", end=" ")
        print(end="")
        # loop for printing
        if r == row//2:
            for i in range((display//2)-1):
                print("*", end=" ")
        else:
            for i in range(display//2):
                print("*", end=" ")
        print(end=" ")
        
        
        display+=2
        esc = row - display 
        print("\n")
       
    else: 
        display-=2
        esc = row - display 
        if r == (row//2) +1:
            continue
        for i in range(display//2):
            print("*", end=" ")
        
        # loop for escaping
        for i in range(esc):
            print(" ", end=" ")
        print(end="")
        
        # loop for printing
        for i in range(display//2):
            print("*", end=" ")
        print(end=" ")
        
        
        print("\n")
    
    
    
