# {
# Driver Code Starts
# Initial Template for Python 3


import math


# } Driver Code Ends

# User function Template for python3

##Complete this function
def modInverse(a, m):
    ##Your code here
    for i in range(1, m):
        if (i * a) % m == 1:
            return i
    else:
        return -1


# {
# Driver Code Starts.


def main():
    T = int(input())

    while (T > 0):
        am = [int(x) for x in input().strip().split()]
        a = am[0]
        m = am[1]
        print(modInverse(a, m))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends    