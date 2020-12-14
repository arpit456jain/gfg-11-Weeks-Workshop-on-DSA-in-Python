#User function Template for python3
import math
class Solution:
    def quadraticRoots(self, a, b, c):
        d = ((b*b) - (4*a*c))
        print(d)
        if d<0:
            lst=[]
            lst.append(-1)
            return lst
        D = math.sqrt(d)
        print(D)
        x1 = math.floor((-1*b + D)/(2*a))
        x2 =  math.floor((-1*b - D)/(2*a))

        print(x1,x2)
        lst = []
        lst.append(int(x1))
        lst.append(int(x2))
        lst.sort()
        lst.reverse()
        print(lst)
        return lst





#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    abc=[int(x) for x in input().strip().split()]
    a=abc[0]
    b=abc[1]
    c=abc[2]
    ob = Solution()
    ans = ob.quadraticRoots(a,b,c)
    if len(ans)==1 and ans[0]==-1:
        print("Imaginary")
    else:
        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()

# } Driver Code Ends