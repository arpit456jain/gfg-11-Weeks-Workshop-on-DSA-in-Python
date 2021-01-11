#User function Template for python3
'''
If the input number is of the form 2^b -1 e.g., 1, 3, 7, 15.. etc,
 the number of set bits is b * 2^(b-1). This is because for all
  the numbers 0 to (2^b)-1, if you complement and flip the list you
   end up with the same list (half the bits are on, half off).
'''
def binaryrepofnum(n):
    for i in range(n):
        print(bin(i)[2:])

def CountBitsinnum(n):
    # code here
    # return the count
    c=0
    while(n>0):
        if n%2 == 1:
            # print("1",end="")
            c=c+1
        else:
            pass
        # n=n//2
        n=n>>1
    # print(c)
    return c
import math
def checkifspecialcase(n):
    n=n+1
    if n&(n-1) == 0:
        return True
    else:
        return False
def CountBits(n):
    c1=0
    if n!= 1 and checkifspecialcase(n):
        print("special case",n)
        logval = int(math.log2(n+1))
        c1 = logval * int(math.pow(2, logval - 1))
    else:
        for i in range(1,n+1):
            # print("in ",i,"->>",CountBitsinnum(i))
            c1=c1+CountBitsinnum(i)
    return c1
#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    # n = int(input("enter n"))
    n=15
    print(CountBits(n))
# } Driver Code Ends