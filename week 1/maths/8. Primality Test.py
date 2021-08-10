""""
A prime number is a number which is only divisible by 1 and itself.
Given number N check if it is prime or not.



Example 1:

Input:
N = 5
Output: Yes
Explanation: 5 is only divisible by 1
and itself. So, 5 is a prime number.
"""

# {
# Driver Code Starts
# Initial Template for Python 3

import math


# } Driver Code Ends
# User function Template for python3
import math
class Solution:
    def isPrime(self, N):
        for i in range(2, int(math.sqrt(N) + 1)):
            if N%i ==0:
                return  False
        else:
            return True

def main():
    T = int(input())

    while (T > 0):

        N = int(input())

        ob = Solution()
        if (ob.isPrime(N)):
            print("Yes")
        else:
            print("No")
        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends