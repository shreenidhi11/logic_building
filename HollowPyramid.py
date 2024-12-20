
N =6
row = N
space = 0

for r in range(row):
    if r == 0:
        print("*", end=" ")
    elif r == row-1:
        print("* "*row)
        print("\n")
    else:
        print("*", end=" ")
        for s in range(space):
            print("_", end=" ")
        # print(end=" ")
        print("*", end=" ")
        space+=1
    print("\n")
  
output:
* 

* * 

* _ * 

* _ _ * 

* _ _ _ * 

* * * * * * 
