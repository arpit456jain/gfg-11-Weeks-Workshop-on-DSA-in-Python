""""
Given a number N, find an integer denoting the smallest number evenly divisible by each number from 1 to n.


Example 1:

Input:
N = 3
Output: 6
Explanation: 6 is the smallest number
divisible by 1,2,3.
"""
import math 
    
# Returns the lcm of first n numbers  
def lcm(n):  
    ans = 1
    for i in range(1, n + 1):  
        ans = int((ans * i)/math.gcd(ans, i))          
    return ans  
class Solution:
    def getSmallestDivNum(self, n):
        # logic is ans is lcm of numbers 1 to n
        ans  = lcm(n)
        return ans



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=1
    for tcs in range(t):
        n=12
        ob = Solution()
        print(ob.getSmallestDivNum(n))
# } Driver Code Ends
