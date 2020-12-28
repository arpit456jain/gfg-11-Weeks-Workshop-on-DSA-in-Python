# User function Template for python3

def getMaxArea(arr):
    n = len(arr)
    maxarea = 0
    stack = []
    limitforleftbar = [None for x in range(n)]
    limitforrightbar = [None for x in range(n)]
    # traverse the array
    for i in range(len(arr)):
        if len(stack) == 0:
            stack.append(i)
            limitforleftbar[i] = 0
        else:
            if len(stack)!=0 and arr[stack[-1]]>=arr[i]:
                while(len(stack)!=0 and arr[stack[-1]]>=arr[i]):
                    stack.pop()
                if len(stack) == 0:
                    limitforleftbar[i] = 0
                else:
                    limitforleftbar[i] = stack[-1] + 1
                stack.append(i)
            else:
                limitforleftbar[i] = i
                stack.append(i)
    stack = []
    for i in range(len(arr)-1,-1,-1):
        if len(stack) == 0:
            stack.append(i)
            limitforrightbar[i] = i
        else:
            if len(stack)!=0 and arr[stack[-1]] >= arr[i]:
                while(len(stack)!=0 and arr[stack[-1]] >= arr[i]):
                    stack.pop()
                if len(stack) == 0:
                    limitforrightbar[i] = n-1
                else:
                    limitforrightbar[i] = stack[-1] - 1
                stack.append(i)
            else:
                limitforrightbar[i] = i
                stack.append(i)
    # now traverse both the limits and find the area
    maxarea = 0
    for i in range(n):
        no_of_bars = limitforrightbar[i] - limitforleftbar[i] + 1
        area = arr[i]*no_of_bars
        if area>maxarea:
            maxarea=area

    return maxarea

def maxArea2(M, n, m):
    #we will find max area of histogram or every row as histogram
    # T.C is very high because i am traversing again and again upward to find height
    # which is wrong i have to optimise this for getting height
    row = len(M)
    col = len(M[0])
    maxarea = 0
    for i in range(row):
        lst = [None for x in range(col)]
        #we have to just  make a array of heights of histogram at every row
        for j in  range(col):
            print(i,j)
            if M[i][j] == 0:
                lst[j] = 0
                print("0 is found", lst)
            elif M[i][j] == 1:
                c = 0
                top = i
                print("top is",top,"and j is ",j)
                while(top>=0 and M[top][j] == 1):
                    c=c+1
                    top = top-1
                lst[j] = c
                print("1 is found",lst)
        area = getMaxArea(lst)
        if area>maxarea:
            maxarea = area
        print("maxarea of",lst,"is",maxarea)
    return maxarea


def maxArea3(M, n, m):
    #this is highly optimised to O(mxn) but still giving tle error
    row = len(M)
    col = len(M[0])
    maxarea = 0
    for i in range(row):
        if i == 0:
            print("first row", M[0])
            area = getMaxArea(M[0])
        else:
            for j in range(col):
                #if first row pas as it is
                if M[i][j] == 1:
                    #agr vo 1 hai to upr wale add kr do
                    M[i][j] = M[i][j] + M[i-1][j]
                else:
                    #agr vo 0 hai to 0 hi rhega
                    pass

            print(i+1,"row ",M[i])
            area = getMaxArea(M[i])
        maxarea = max(maxarea,area)
        print("maxarea of",M[i],"is",maxarea)

    return maxarea

def maxArea(M, n, m):
    #this is highly optimised to O(mxn) and clear and neat
    # but still giving tle error
    row = len(M)
    col = len(M[0])
    maxarea = 0
    lst = [0*x for x in range(col)]
    for i in range(row):
        for j in range(col):
            if M[i][j] == 0:
                lst[j] = 0
            else:
                lst[j] += 1
        # print(lst)
        maxarea = max(maxarea,getMaxArea(lst))

        # print("for row",i+1,"area is",maxarea)

    return maxarea
if __name__ == '__main__':
    # t = int(input())
    t=1
    for _ in range(t):
        R, C = input().split()
        a = list(map(int, input().split()))
        j = 0
        A = []
        R = int(R)
        C = int(C)
        # R = 4
        # C = 5
        for i in range(0, R):
            A.append(a[j:j + C])
            j = j + C

        # A = [[1,0,1,0,0],
        #     [1,0,1,1,1],
        #      [1,1,1,1,1],
        #      [1,0,0,1,0]
        #      ]

        print(maxArea(A, R, C))

