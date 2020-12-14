# User function Template for python3

def subArraySum(arr, n, sum):
    # Your code here
    cursum = arr[0]
    l = 0
    lst = []
    for i in range(1, n):
        cursum = cursum + arr[i]
        # print(cursum)
        if cursum > sum:
            cursum = cursum - arr[l]
            l = l + 1
        if cursum == sum:
            # lst.append(l+1)
            # lst.append(i+1)
            print(l + 1, i + 1)
            # return lst
    else:
        return -1


# {
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):
        NS = input().strip().split()
        N = int(NS[0])
        S = int(NS[1])

        A = list(map(int, input().split()))

        subArraySum(A, N, S)

        print()

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends