#User function Template for python3
'''
Function Arguments :
		@param  : histogram( given list containing info about histogram)
		@return : integer
'''
def getMaxArea(arr):
    n = len(arr)
    print(arr, n)
    maxarea = 0
    stack = []
    limitforleftbar = [None for x in range(n)]

    limitforrightbar = [None for x in range(n)]
    # traverse the array
    for i in range(len(arr)):
        print(i)
        # find left bar less than current
        # print("left bar")

        if len(stack) == 0:
            print("stack is empty")
            stack.append(i)
            limitforleftbar[i] = 0
        else:
            print("stack is not empty ",stack)
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
        print("left limits",limitforleftbar,"and stack is",stack)
    stack = []
    for i in range(len(arr)-1,-1,-1):
        print(i)
        #find right bar less than current
        # print("right bar")
        if len(stack) == 0:
            print("stack is empty")
            stack.append(i)
            limitforrightbar[i] = i
            print("right limits",limitforrightbar,"and stack is\n",stack)
        else:
            print("stack is not empty",stack)
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
            print("right limits",limitforrightbar,"and stack is\n",stack)
    # now traverse both the limits and find the area
    maxarea = 0
    for i in range(n):
        no_of_bars = limitforrightbar[i] - limitforleftbar[i] + 1
        area = arr[i]*no_of_bars
        if area>maxarea:
            maxarea=area
        print("for bar ",i,"no of bars covered",no_of_bars,"and area is",area)
    return maxarea

def getMaxArea2(arr):
    # naive approch :
    n = len(arr)
    print(arr,n)
    maxarea = 0
    #traverse the array
    for i in range(len(arr)):

        #find left bar less than current
        print("left bar")
        leftcur = i
        while(arr[leftcur]>=arr[i] and leftcur>=0):
            # print("current pos is",leftcur,"and current element is",arr[leftcur])
            leftcur = leftcur - 1
        leftcur=leftcur+1
        print("final pos of left",leftcur)
        print("right bar")
        #find right bar less than current
        rightcur = i
        while(rightcur<n and arr[rightcur]>=arr[i]):
            # print("current pos is", rightcur, "and current element is", arr[rightcur])
            rightcur = rightcur + 1
        rightcur=rightcur-1
        print("final pos of right",rightcur)

        width = rightcur - leftcur + 1
        area = arr[i] * width
        print("width for ",arr[i]," is ",width,"and area is ",area)
        if area>maxarea:
            maxarea=area
        print()
    return maxarea

if __name__ == '__main__':
    # t = int(input())
    t=1
    for cases in range(t) :
        n = int(input())
        # n=7
        a = list(map(int,input().strip().split()))
        # a = [7, 2 ,8 ,9 ,1 ,3 ,6, 5]
        # a = [6,2,5,4,5,1,6]
        print(getMaxArea(a))
# } Driver Code Ends