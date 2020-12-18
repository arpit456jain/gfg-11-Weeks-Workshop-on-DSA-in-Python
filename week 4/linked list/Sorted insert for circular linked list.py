# User function Template for python3
def getTailPointer(head):
    tail = head
    while(tail.next!=head):
        tail = tail.next
    return tail
def sortedInsert(head, data):
    current = head
    prev = head
    newnode= Node(data)
    # if 1st node is greater than data
    tail1 = getTailPointer(head)
    if data<=head.data:
        newnode.next = head
        head = newnode
        tail1.next = head
        return head
    while(current.next!=head):
        if data <= current.data:
            prev.next = newnode
            newnode.next = current
            return head
        prev = current
        current=current.next
    if data>=current.data:
        current.next = newnode
        newnode.next = head
    return head
# contributed by Arpit jain
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None
        self.last = None

    # Function to insert a new node
    def push(self, data):
        if not self.head:
            nn = Node(data)
            self.head = nn
            self.last = nn
            nn.next = nn
            return
        nn = Node(data)
        nn.next = self.head
        self.last.next = nn
        self.last = nn

    # Utility function to print the linked LinkedList


def printList(head):
    if not head:
        return
    temp = head
    print(temp.data, end=' ')
    temp = temp.next
    while (temp != head):
        print(temp.data, end=' ')
        temp = temp.next


if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        data = int(input())

        cll = LinkedList()
        for e in arr:
            cll.push(e)

        reshead = sortedInsert(cll.head, data)
        printList(reshead)
        print()

# } Driver Code Ends