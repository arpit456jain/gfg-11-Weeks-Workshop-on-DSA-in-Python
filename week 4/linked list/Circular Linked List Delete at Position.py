# User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
def getTailPointer(head):
    tail = head
    while(tail.next!=head):
        tail = tail.next
    return tail
def getlen(head):
    count=0
    t = head
    while(t.next!=head):
        count+=1
        t = t.next
    count=count+1
    return count
def delAtBeg(head,len1):
    # print("inside del at beg")
    if len1 == 1:
        head = None
        # return head
    elif len1 == 2:
        sendnode = head.next
        sendnode.next = head.next
        head = sendnode
        # return head
    else:
        tail1 = getTailPointer(head)
        # print("tail pointer is at",tail1.data)
        temp = head
        tail1.next = temp.next
        head = temp.next
        del temp
    return head

def delAtEnd(head,len1):
    cur = head
    while(cur.next!=head):
        prev = cur
        cur = cur.next
    # print("prev pointer is at",prev.data)
    prev.next = head
    return head
def deleteAtPosition(head, pos):
    i=1
    l1 = getlen(head)
    # print("count of node",l1,"and pos to be deleted",pos)
    current = head
    if pos == 1:
        # print("pos is 1")
        head = delAtBeg(head,l1)
    elif pos == l1:
        delAtEnd(head,l1)
    else:
        # print("pos is in between")
        while(i<pos-1):
            # print(current.data)
            current=current.next
            i=i+1
        newnode = current.next
        current.next = newnode.next
        del newnode
    return head
# contributed by Arpit Jain
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Llist:
    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)

        if not self.head:
            self.head = node
            return node

        tail.next = node
        return node


def displayList(head):
    t = head
    while t.next != head:
        print(t.data, end=' ')
        t = t.next

    print(t.data, end=' ')


if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):

        n = int(input())
        arr = [int(x) for x in input().split()]
        pos = int(input())

        ll = Llist()
        tail = None

        for nodeData in arr:
            tail = ll.insert(nodeData, tail)
        # making circular
        tail.next = ll.head

        resHead = deleteAtPosition(ll.head, pos)
        displayList(resHead)
        print()
# } Driver Code Ends