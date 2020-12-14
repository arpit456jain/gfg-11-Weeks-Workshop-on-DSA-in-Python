# User function Template for python3

import math


# Complete this function
def floorSqrt(x):
    # Your code here
    y = int(math.pow(x, 1 / 2))
    return y


# {
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):
        x = int(input())

        print(floorSqrt(x))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends