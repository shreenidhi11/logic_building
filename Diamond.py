# print pyramid
r = 5
prevc = 0
leavec = r - 0 - 1
for i in range(r):
    if i <= r//2:
        # leavec = r - i-1
        for l in range(leavec):
            print(" ",end="")
        for p in range(2*i+1):
            print("*",end="")
        print("\n")
        prevc = 2*i+1
        leavec-=1
    else:
        prevc-=2
        leavec+=1
        for l in range(leavec+1):
            print(" ",end="")
        for p in range(prevc):
            print("*",end="")
        print("\n")

# output 
    *

   ***

  *****

   ***

    *
