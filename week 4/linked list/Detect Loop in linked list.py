# User function Template for python3
'''
	Your task is to detect if any loop is present
	in the given linked list.

	Function Arguments: head (reference to head of the linked list)
	Return Type: True or False (boolean)

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''


def detectLoop(head):
    c=0
    while(head!=None):
        c=c+1
        if c>100:
            return True
        head = head.next
    return False

def detectloop(head):
    #not efficient method but works 100%
    lst = []
    while(head!=None):
        if head in lst:
            return True
        lst.append(head)
        head = head.next
    return False
def detectloop2(head):
    #by floyds cycle finding method which is nost effiecient
    slow = head
    fast = head
    while(slow and fast and fast.next):
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
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

    # connects last node to node at position pos from begining.
    def loopHere(self, pos):
        if pos == 0:
            return

        walk = self.head
        for i in range(1, pos):
            walk = walk.next

        self.tail.next = walk


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())

        LL = LinkedList()
        for i in input().split():
            LL.insert(int(i))

        LL.loopHere(int(input()))

        print(detectloop2(LL.head))
# } Driver Code Ends