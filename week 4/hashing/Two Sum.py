'''
Given an array of positive integers and an integer. Determine whether or not there exist two elements in A whose sum is exactly equal to that integer.
'''
#User function Template for python3

# A[] : the input array of positive integers
# N : size of the array arr[]
# X : the required sum
def keypair(A, N, X):
    A.sort()
    i=0 # from starting
    j=N-1 #from end
    while(i<j):
        sum1 = A[i] + A[j]
        if sum1>X:
            j=j-1
            continue
        if sum1 == X:
            return True
        i=i+1
    return False

t=int(input())
for _ in range(0,t):
    n,x=list(map(int,input().split()))
    a=list(map(int,input().split()))
    sln=keypair(a,n,x)
    if(sln):
        print("Yes")
    else:
        print("No")
# } Driver Code Ends