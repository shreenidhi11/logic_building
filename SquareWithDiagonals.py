# the value of r and c can be any same integer value
r,c = 10,10

cc = c-1

for rows in range(r):
    for cols in range(c):
        if rows == 0 or rows == r-1 or rows == cols or cols == cc:
            print("*",end=" ")
        else:
            if cols == 0 or cols == c-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print("\n")
    cc -=1

# output produced is a below
* * * * * * * * * * 

* *             * * 

*   *         *   * 

*     *     *     * 

*       * *       * 

*       * *       * 

*     *     *     * 

*   *         *   * 

* *             * * 

* * * * * * * * * * 
