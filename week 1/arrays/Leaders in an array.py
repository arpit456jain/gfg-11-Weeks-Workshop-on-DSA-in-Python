# User function Template for python3

def leaders(arr, size):
    maxlst = []
    max_from_right = arr[size - 1]
    maxlst.append(max_from_right)
    for i in range(size - 2, -1, -1):
        if max_from_right <= arr[i]:
            maxlst.append(arr[i])
            max_from_right = arr[i]

    maxlst.reverse()
    return maxlst


# {
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():
    T = int(input())

    while (T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]

        A = leaders(A, N)

        for i in A:
            print(i, end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends