# {
# Driver Code Starts
# Initial Template for Python 3

import math


# } Driver Code Ends

# User function Template for python3

# Compelte his function
def termOfGP(A, B, N):
    # Your code here
    r = B / A
    ans = A * ((math.pow(r, N - 1)))
    # print(r,ans)
    return ans


# {
# Driver Code Starts.
def main():
    T = int(input())

    while (T > 0):
        AB = [int(x) for x in input().strip().split()]
        A = AB[0]
        B = AB[1]

        N = int(input())

        print(math.floor(termOfGP(A, B, N)))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends