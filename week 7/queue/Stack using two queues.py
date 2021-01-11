# User function Template for python3
'''
    :param x: value to be inserted
    :return: None

    queue_1 = [] # first queue
    queue_2 = [] # second queue
    '''


def push(x):
    # global declaration
    global queue_1
    global queue_2

    # code here
    queue_1.append(x)
    # print(queue_1,queue_2)

def pop():
    '''
    :return: the value of top of stack and pop from it.
    '''
    # global declaration
    global queue_1
    global queue_2
    if len(queue_1) == 0:
        return -1
    elif len(queue_1)==1:
        return queue_1.pop(0)
    else:

        while(len(queue_1)!=1):
            pi = queue_1.pop(0)
            queue_2.append(pi)
        res = queue_1.pop(0)
        queue_2,queue_1=queue_1,queue_2
        # print(queue_1,queue_2)
        return res



queue_1 = []  # first queue
queue_2 = []  # second queue

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        i = 0
        while i < len(a):
            if a[i] == 1:
                push(a[i + 1])
                i += 1
            else:
                print(pop(), end=" ")
            i += 1

        # clear both the queues
        queue_1 = []
        queue_2 = []
        print()
# } Driver Code Ends