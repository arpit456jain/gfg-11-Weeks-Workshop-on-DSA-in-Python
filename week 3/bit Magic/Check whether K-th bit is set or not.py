# {
# Driver Code Starts
# Initial Template for Python 3

import math


# } Driver Code Ends

# User function Template for python3

##Complete this code
def checkKthBit(n, k):
    mask = 1<<k
    if mask&n>0:
        return True
    else:
        return False

def main():
    T = int(input())

    while (T > 0):

        n = int(input())
        k = int(input())

        if checkKthBit(n, k):
            print("Yes")
        else:
            print("No")

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends