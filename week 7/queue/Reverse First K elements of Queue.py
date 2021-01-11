#User function Template for python3
'''
Function Arguments :
		@param  : queue ( given queue to be used), k(Integer ),n(size of queue)
		@return : lsit, just reverse the first k elements of queue and return new queue
'''
def enqueue(lst,item):
    #insert at last
    lst.append(item)

def dequeue(lst):
    #remove 1st item
    item = lst.pop(0)
    # lst[:] = lst[1:]

    return item
def reverseK(queue,k,n):
    #first deque k elements from queue and push them into stack
    stack = []
    for i in range(0,k):
        d_item = dequeue(queue)
        stack.append(d_item)
    # print(queue,stack)

    #then pop all elements from stack and enque to queue
    while(len(stack)!=0):
        pi = stack.pop()
        enqueue(queue,pi)
    # print(queue,stack)

    #now deque the remaining item and add them at last
    for i in range(0,len(queue)-k):
        d_item = dequeue(queue)
        enqueue(queue,d_item)
    # print(queue,stack)
    return queue



if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))

        queue = [] # our queue to be used
        for i in range(n):
            queue.append(a[i]) # enqueue elements of array in our queue

        print(*reverseK(queue,k,n))
# } Driver Code Ends