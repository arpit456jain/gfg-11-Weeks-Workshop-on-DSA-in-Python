# User function Template for python3
import copy
def multiplyMatrix(A, B):
    # code here

    m=len(A)
    n = len(A[0])
    n2 = len(B)
    l = len(B[0])

    a= [[0 for x in range(l)]
           for y in range(m)]
    # print(m,n,n2,l,a)
    if n==n2:
        for i in range(0,m):
            for j in range(0,l):
                # print(i,j)
                a[i][j]=0
                for k in range(0,n):
                    a[i][j] = a[i][j] + A[i][k]*B[k][j]

    else:
        a=[]
        return a
    # print(a)
    return a


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        n1, m1 = map(int, input().strip().split())
        A = [[0 for j in range(m1)] for i in range(n1)]
        line1 = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(n1):
            for j in range(m1):
                A[i][j] = line1[k]
                k += 1

        n2, m2 = map(int, input().strip().split())
        B = [[0 for j in range(m2)] for i in range(n2)]
        line2 = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(n2):
            for j in range(m2):
                B[i][j] = line2[k]
                k += 1

        ans = multiplyMatrix(A, B)

        if (len(ans) == 0):
            print(-1)
        else:
            for i in range(len(ans)):
                for j in range(len(ans[0])):
                    print(ans[i][j], end=' ')
            print()

            # } Driver Code Ends