"""  list Node is as defined below:

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None

"""


# complete this function
# return head of list after swapping

def pairWiseSwap(head):
    if head == None:
        return head
    if head.next == None:
        return head
    if head.next.next == None:
        head.data,head.next.data = head.next.data,head.data
        return head
    prev = head
    cur = head.next
    try:

        while(cur!=None):
            prev.data,cur.data = cur.data,prev.data
            prev = prev.next.next
            cur = cur.next.next
    except:
        return head
    return head

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next


def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]

        lis = LinkedList()
        for i in arr:
            lis.insert(i)

        head = pairWiseSwap(lis.head)
        printList(head)

# } Driver Code Ends