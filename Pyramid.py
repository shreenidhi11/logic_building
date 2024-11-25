# print pyramid
r = 10

for i in range(r):
    leave = r - i-1
    for l in range(leave):
        print(" ",end="")
    prints = r-leave
    for p in range(prints):
        print("*",end="")
    
    for _ in range(i):
        print("*",end="")
    
    print("\n")

# output
   *

  ***

 *****

*******
