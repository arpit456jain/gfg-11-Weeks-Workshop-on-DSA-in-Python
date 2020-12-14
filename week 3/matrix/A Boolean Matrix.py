# Driver Code
def printMatrix(lst2):
    for i in range(len(lst2)):
        for j in range(len(lst2[0])):
            print(lst2[i][j],end=" ")
        print()
import copy

def modifyMatrix2(temp):
    #we do not use any extra matrxi here and TC is also optimised
    row = len(temp)
    col = len(temp[0])
    rowlst = [int(i*0) for i in range(row)]
    collst = [int(i*0) for i in range(col)]
    print(rowlst,collst)
    for i in range(row):
        for j in range(col):
            if temp[i][j] == 1:
                # change 0 in row
                if rowlst[i] != 1:
                    r = i
                    for k in range(col):
                        temp[r][k] = -1
                    rowlst[i] = 1
                if collst[j] !=1:
                    # change in col
                    c = j
                    for l in range(row):
                        temp[l][c] = -1
                    collst[j] = 1
    for i in range(row):
        for j in range(col):
            if temp[i][j] == -1:
                temp[i][j] = 1
def modifyMatrix(lst1):
    # TC : O(m*n)*(m+n)
    # A.s  = o(mxn)
    row = len(lst1)
    col = len(lst1[0])
    temp = copy.deepcopy(lst1)
    for i in range(row):
        changeinrow = False
        for j in range(col):
            if temp[i][j] == 1:
                #change 0 in row
                if changeinrow !=True:
                    r=i
                    for k in range(col):
                        lst1[r][k]=1
                    changeinrow=True
                #change in col
                c=j
                for l in range(row):
                    lst1[l][c]=1

mat = [[1, 0, 0, 1],
       [0, 0, 1, 0],
       [0, 0, 0, 0]]

print("Input Matrix n")
printMatrix(mat)

modifyMatrix2(mat)

print("Matrix after modification n")
printMatrix(mat)