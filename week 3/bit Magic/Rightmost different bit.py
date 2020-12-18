# {
# Driver Code Starts
# Initial Template for Python 3

import math


def posOfRightMostDiffBit(a,b):
    if a > b:
        a, b = b, a
    i=1
    while (b > 0):

        if (a % 2) == (b % 2):
            pass
        else:
            return i
        a = a // 2
        b = b // 2
        i=i+1

def main():
    T = int(input())

    while (T > 0):
        mn = [int(x) for x in input().strip().split()]
        m = mn[0]
        n = mn[1]

        print(math.floor(posOfRightMostDiffBit(m, n)))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends