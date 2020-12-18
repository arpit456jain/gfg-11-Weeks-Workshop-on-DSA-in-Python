# User function Template for python3

def rotateby902(a, n):
    for i in range(0,n//2):
        for j in range(i,n-1-i):
            temp = a[i][j]

            a[i][j] = a[j][n-1-i]
            a[j][n - 1 - i] = a[n-1-i][n-1-j]
            a[n - 1 - i][n - 1 - j] = a[n-1-j][i]
            a[n-1-j][i] = temp

    return a
import copy
def rotateby90(a, n):
    temp = copy.deepcopy(a)
    for i in range(0,n):
        for j in range(0,n):
            a[i][j] = temp[j][n-i-1]

# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix = [[0 for j in range(n)] for i in range(n)]
        line1 = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(n):
            for j in range(n):
                matrix[i][j] = line1[k]
                k += 1

        rotateby90(matrix, n)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j], end=" ")
        print()

# } Driver Code Ends