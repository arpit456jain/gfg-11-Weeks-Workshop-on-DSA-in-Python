# function Template for python3

"""
# Node Class

class node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""


# This function should reverse linked list and return
# head of the modified linked list
def reverseList(head):
    head2=None
    while(head!=None):
        if head2==None:
            head2 = Node(head.data)
        else:
            tmp = Node(head.data)
            tmp.next = head2
            head2 = tmp
        # print(head2, head2.data)
        head = head.next
    return head2

def reverseList2(head):
    cur=head
    prev = None
    next1 = None
    while(cur!=None):
        next1 = cur.next
        cur.next = prev
        prev = cur
        cur = next1
    head  = prev
    return head


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


# Linked List Class
class Linked_List:
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


def printList(head):
    tmp = head
    while tmp:
        print(tmp.data, end=' ')
        tmp = tmp.next
    print()


if __name__ == '__main__':
    for i in range(1):
        # n = int(input())
        n=6
        # arr = [int(x) for x in input().split()]
        arr = [1,2,3,4,5,6]
        lis = Linked_List()
        for i in arr:
            lis.insert(i)

        newHead = reverseList2(lis.head)
        printList(newHead)

