""""
Given the first 2 terms A and B of a Geometric Series. The task is to find the Nth term of the series.

Example 1:

Input:
A = 2
B = 3
N = 1
Output: 2
Explanation: The first term is already
given in the input as 2
"""
import math
class Solution:
    # Compelte his function
    def termOfGP(self, A, B, N):
        # Your code here
        r = B / A
        ans = A * ((math.pow(r, N - 1)))
        # print(r,ans)
        return ans



def main():
    T = int(input())

    while (T > 0):
        AB = [int(x) for x in input().strip().split()]
        A = AB[0]
        B = AB[1]

        N = int(input())
        ob = Solution()
        print(math.floor(ob.termOfGP(A, B, N)))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends