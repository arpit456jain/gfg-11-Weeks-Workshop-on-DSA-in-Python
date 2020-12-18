# {
# Driver Code Starts
# Initial Template for Python 3

import math


# } Driver Code Ends

# User function Template for python3

##Complete this function
def getFirstSetBit(n):
    i=0
    if n == 0:
        return 0
    while(n>0):
       if n%2 == 1:
           return i+1
       i=i+1
       n=n//2

def main():
    T = int(input())

    while (T > 0):
        n = int(input())

        print(getFirstSetBit(n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends