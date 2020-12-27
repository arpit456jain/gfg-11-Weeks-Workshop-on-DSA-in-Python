#User function Template for python3


def nextLargerElement2(arr,n):
    # t.c = O(n^2)
    maxelement = []
    for i in range(n):
        max1 = -1
        for j in range(i+1,n):
            print(i,j)
            if arr[j] > arr[i]:
                max1 = arr[j]
                print("for ",arr[i],"next element is",max1)
                maxelement.append(max1)
                break
        else:
            print("for ", arr[i], "next element is",-1)
            maxelement.append(-1)

    return maxelement
def nextLargerElement(arr,n):
    # T.C = O(n)
    next = [0*x for x in range(n)]
    stack1 = []
    stack1.append(0)
    for i in range(1,n):
        print(i,stack1,next)
        if len(stack1) == 0:
            stack1.append(i)
            continue
        #push every item if it is smaller than or equal to
        print("stack is not empty and arr[i] is ",arr[i],"and arr[stack1[-1]] is ",arr[stack1[-1]])
        if arr[i]<= arr[stack1[-1]]:
            stack1.append(i)
            print("aftr just pushing simply",stack1)
            continue
        #now we got a element which is greater than top so push every element
        #until top is greater than cur
        print("now we got an element which is greater than top",stack1,arr[i])
        while(len(stack1)!=0 and arr[i]>arr[stack1[-1]]):
            print("after poping stack[-1]",stack1[-1])
            popped_index = stack1.pop()
            next[popped_index] = arr[i]
            print("after inserting in next",stack1,next)

        stack1.append(i)

    #now the remaining indexes in stack have -1 because no element is greater than it
    while(len(stack1)!=0):
        popped_index = stack1.pop()
        next[popped_index] = -1

    return next
if __name__ == '__main__':
    t = int(input())
    # t = 1
    for cases in range(t) :
        n = int(input())
        # n = 4
        a = list(map(int,input().strip().split()))
        # a = [1,3,2,4]
        res = nextLargerElement(a,n)
        for i in range (len (res)):
            print (res[i], end = " ")
        print ()
# } Driver Code Ends