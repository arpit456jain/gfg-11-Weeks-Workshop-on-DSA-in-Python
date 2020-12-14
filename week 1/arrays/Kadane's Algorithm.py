# User function Template for python3

##Complete this function
def maxSubArraySum(a, size):
    ##Your code here
    max_so_far = 0
    max_ending_here = 0
    for i in a:
        max_ending_here=max_ending_here+i
        if max_so_far<max_ending_here:
            max_so_far=max_ending_here
        if max_ending_here<0:
            max_ending_here=0
    return max_so_far



# {
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):
        n = int(input())

        arr = [int(x) for x in input().strip().split()]

        print(maxSubArraySum(arr, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends