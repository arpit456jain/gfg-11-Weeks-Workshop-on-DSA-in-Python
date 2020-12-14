# User function Template for python3

# T.C = O(n*m)
def search2(matrix, n, m, x):
    # code here
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 54:
                return True
    return 0
def search(matrix, n, m, x):
    i=0
    j=m-1
    # print(n,m,i,j)
    while(i<n and j>=0):
        # print("in loop")
        if matrix[i][j] == x:
            return True
        elif matrix[i][j]>x:
            # means element is in current row so decrease colomn
            # print("element is in current row so decrease colomn")
            j=j-1
        else:
            # means elememt is in next row so increase row
            # print("elememt is in next row so increase row")
            i=i+1
    return 0

# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        size = input().strip().split()
        r = int(size[0])
        c = int(size[1])
        line = input().strip().split()
        matrix = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                matrix[i][j] = int(line[i * c + j])
        target = int(input())

        if (search(matrix, r, c, target)):
            print(1)
        else:
            print(0)

            # } Driver Code Ends