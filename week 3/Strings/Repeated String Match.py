# User function Template for python3
import math


def repeatedStringMatch(A, B):
    times = int(math.ceil(float(len(B)) / len(A)))
    for i in range(2):

        if B in (A * (times + i)):
            return times + i
    return -1


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        A = input().strip()
        B = input().strip()
        print(repeatedStringMatch(A, B))
# } Driver Code Ends