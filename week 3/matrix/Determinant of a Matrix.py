#User function Template for python3
import numpy as np
def determinantOfMatrix(matrix,n):
    # calling the det() method
    det = np.linalg.det(matrix)
    det = round(det)
    return int(det)

if __name__ == '__main__':
    # t = int(input())
    t=1
    for _ in range(t):
        n = int(input())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(n):
            row=[]
            for j in range(n):
                row.append(values[k])
                k+=1
            matrix.append(row)
    #     matrix = [[1, 2], [3, 4]]
        # n=2
        print(determinantOfMatrix(matrix,n))
# } Driver Code Ends