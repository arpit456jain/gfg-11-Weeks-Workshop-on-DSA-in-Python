#User function Template for python3

import math 
    
# Returns the lcm of first n numbers  
def lcm(n):  
    ans = 1
    for i in range(1, n + 1):  
        ans = int((ans * i)/math.gcd(ans, i))          
    return ans  
class Solution:
    def getSmallestDivNum(self, n):
        #hme inka lcm nikalna hoga aur uske liye gcd ka use kreger
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
