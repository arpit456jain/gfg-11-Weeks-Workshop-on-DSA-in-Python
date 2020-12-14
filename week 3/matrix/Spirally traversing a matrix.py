# User function Template for python3

def spirallyTraverse(A, r, c):
    # code here
    k = 0
    l = 0
    m = r
    n = c
    lst = []
    while (k < m and l < n):
        print(" upper row")
        for i in range(l, n):
            print(A[k][i],end=" ")
            lst.append(A[k][i])
        k = k + 1
        print("left col")
        for i in range(k, m):
            print(A[i][n-1])
            lst.append(A[i][n - 1])
        n = n - 1

        if (k < m):
            print(' bottm row')
            for i in range(n - 1, l-1, -1):
                # print(i)
                print(A[m-1][i])
                lst.append(A[m - 1][i])

            m = m - 1
        if l<n:
            print('right col')
            for i in range(m-1,k-1,-1):
                print(A[i][l])
                lst.append(A[i][l])
            l=l+1
    return lst


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r, c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix = []
        for i in range(r):
            row = []
            for j in range(c):
                row.append(values[k])
                k += 1
            matrix.append(row)
        ans = spirallyTraverse(matrix, r, c)
        for i in ans:
            print(i, end=" ")
        print()

# } Driver Code Ends
