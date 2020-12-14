# User function Template for python3

def rotateArr(A, D, N):
    # Your code here
    lst = A[0:D]
    # print(lst)
    for i in range(0, N - D):
        A[i] = A[i + D]
    A[N - D:] = lst[:]
    return A


# {
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():
    T = int(input())

    while (T > 0):
        nd = [int(x) for x in input().strip().split()]
        N = nd[0]
        D = nd[1]
        A = [int(x) for x in input().strip().split()]

        rotateArr(A, D, N)

        for i in A:
            print(i, end=" ")

        print()

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends