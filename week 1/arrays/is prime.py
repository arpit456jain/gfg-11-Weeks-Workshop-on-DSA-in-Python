# {
# Driver Code Starts
# Initial Template for Python 3

import math


# } Driver Code Ends

# User function Template for python3
# Python program to print all primes smaller than or equal
def isPrime(n):
    # Corner cases
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6

    return True


# {
# Driver Code Starts.
def main():
    T = int(input())

    while (T > 0):

        N = int(input())

        if (isPrime(N)):
            print("Yes")
        else:
            print("No")
        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends