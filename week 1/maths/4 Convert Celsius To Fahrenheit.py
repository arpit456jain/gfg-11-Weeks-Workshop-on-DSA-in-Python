""""
Given a temperature in celsius C. You need to convert the given temperature to Fahrenheit.

Example 1:

Input:
C = 32
Output: 89
Explanation: Using the conversion
formula of celsius to farhenheit , it
can be calculated that, for 32 degree
C, the temperature in Fahrenheit = 89.
"""
# (0°C × 9/5) + 32 = 32°F

import math


# } Driver Code Ends
# User function Template for python3

class Solution:
    ##Complete this function
    def cToF(self, C):
        # (0°C × 9/5) + 32 = 32°F
        return (C*9)/5 + 32


# Your code here


# {
# Driver Code Starts.
def main():
    T = int(input())

    while (T > 0):
        C = int(input())
        ob = Solution()
        print(math.floor(ob.cToF(C)))
        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends