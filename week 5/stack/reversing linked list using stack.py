# Python3 program to print reverse
# of a linked list
def printrevbystack(head):
    print("by stack")
    stack  = ['N']
    temp = head
    while(temp!=None):
        stack.append(temp.data)
        temp = temp.next
    while(stack[-1]!='N'):
        print(stack.pop(),end=" ")

def printrev(head2):
    if head2.next == None:
        print(head2.data)
        return
    else:
        printrev(head2.next)
    print(head2.data)
    return

def printll(head):
    temp = head
    while(temp!=None):
        print(temp.data,end=" ")
        temp = temp.next
    print()
# Node class
class Node:

    # Constructor to initialize
    # the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None


    # Function to insert a new node
    # at the beginning
    def push(self, new_data):

        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Driver code


llist = LinkedList()
for i in range(5,0,-1):
    llist.push(i)
# print(llist,llist.head,llist.head.data)
printll(llist.head)
printrev(llist.head)
# printrevbystack(llist.head)
