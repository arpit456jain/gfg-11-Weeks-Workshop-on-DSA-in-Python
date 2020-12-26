'''
Definition for singly linked list
class Node:
    def __init__(self,x):
        self.val=x
        self.nxt=None
'''


def rotate(head, k):
    temp = head
    c=0
    prev = head
    while(temp!=None):
        c=c+1
        prev = temp
        temp = temp.nxt

    # print(c)
    k=k%c
    if k == 0:
        return head
    prev.nxt = head
    diff=c-k
    temp = head
    prev2 = head
    while(diff>0):
        # print(temp.val)
        diff = diff-1
        prev2 = temp
        temp = temp.nxt
    prev2.nxt = None
    head = temp
    return head
class Node:
    def __init__(self, x):
        self.val = x
        self.nxt = None


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        line = input().strip().split()
        k = int(input())

        head = Node(int(line[0]))
        tail = head
        for i in range(1, n):
            tail.nxt = Node(int(line[i]))
            tail = tail.nxt

        head = rotate(head, k)

        while (head):
            print(head.val, end=' ')
            head = head.nxt
        print()

# } Driver Code Ends