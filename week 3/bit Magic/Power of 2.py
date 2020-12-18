# User function Template for python3


##Complete this function
def isPowerofTwo(n):
    ##Your code here
    if n == 0:
        return False
    if n & (n - 1) == 0:
        return True
    else:
        return False


# {
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():
    T = int(input())

    while (T > 0):

        n = int(input())
        if isPowerofTwo(n):
            print("YES")
        else:
            print("NO")

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends