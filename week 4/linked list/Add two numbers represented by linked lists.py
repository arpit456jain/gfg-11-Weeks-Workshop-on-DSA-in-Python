# User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
# Contributrd by Arpit Jain
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

def addLists(first, second):
    first = reverseList2(first)
    second = reverseList2(second)
    LL3 = LinkedList()
    # LL1.insert(i) for inserting
    c=0
    while(first!=None and second!=None):
        if c==1:
            sum1 = first.data + second.data + 1
            c=0
        else:
            sum1 = first.data + second.data
        if sum1>=10:
            c=1
            sum1 = sum1 % 10
        LL3.insert(sum1)
        first = first.next
        second = second.next

    if first == None:
        while(second!=None):
            if c==1:
                sum1 = second.data + 1
                c=0
            else:
                sum1 = second.data
            if sum1 >=10:
                sum1 = sum1%10
                c=1
            LL3.insert(sum1)
            second = second.next
    elif second == None:
        while (first!= None):
            # print("first list continue",first.data,c)
            if c==1:
                sum1 = first.data + 1
                c=0
            else:
                sum1 = first.data
            if sum1 >=10:
                sum1 = sum1%10
                c=1

            LL3.insert(sum1)
            first = first.next
    else:
        print("eror")

    # print(c)
    if c == 1:
        LL3.insert(c)
    LL3.head = reverseList2(LL3.head)
    return LL3.head

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next


# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()


if __name__ == '__main__':
    for _ in range(int(input())):

        n = int(input())
        arr1 = (int(x) for x in input().split())
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)

        m = int(input())
        arr2 = (int(x) for x in input().split())
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)

        res = addLists(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends