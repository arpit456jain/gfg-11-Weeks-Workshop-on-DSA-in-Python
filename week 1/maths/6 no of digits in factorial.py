"""
Given an integer N. Find the number of digits that appear in its factorial.
Factorial is defined as, factorial(n) = 1*2*3*4……..*N and factorial(0) = 1.


Example 1:

Input: N = 5
Output: 3
Explanation: Factorial of 5 is 120.
Number of digits in 120 is 3 (1, 2, and 0)
"""


def logOFfact(n):
    ans=0
    for i in range(1,n+1):
        ans = ans + math.log10(i)
    return ans


# User function Template for python3

class Solution:
    def digitsInFactorial(self, n):
        x = logOFfact(n)

        return math.floor(x) + 1;


import math

def main():
    T = int(input())

    while (T > 0):
        N = int(input())
        ob = Solution()
        print(ob.digitsInFactorial(N))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends