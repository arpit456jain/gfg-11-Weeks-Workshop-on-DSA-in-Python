#User function template for Python

class Solution:
	def remove_duplicate(self, A, N):
		# code here
		A[:] = list(set(A))
		#print(lst)
		A.sort()
		return len(A)



#{
#  Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        n = ob.remove_duplicate(A,N)
        for i in range(n):
            print(A[i], end=" ")
        print()


# } Driver Code Ends