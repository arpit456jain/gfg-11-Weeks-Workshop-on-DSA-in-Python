# User function Template for python3

def push(arr, n):
# return a queue with all elements of arr inserted in it
    return arr


def _pop(q):
# dequeue elements and print them
    for i in q:
        print(i,end=" ")

def deque():
    return None

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        q = deque()
        q = push(arr, n)
        _pop(q)
        print()
# } Driver Code Ends