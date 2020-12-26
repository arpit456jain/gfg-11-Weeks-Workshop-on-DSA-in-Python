# Python program to split circular linked list into two halves
import math
# A node structure
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None


# Class to create a new Circular Linked list
class CircularLinkedList:

    # Constructor to create a empty circular linked list
    def __init__(self):
        self.head = None

    # Function to insert a node at the beginning of a
    # circular linked list
    def push(self, data):
        ptr1 = Node(data)
        temp = self.head

        ptr1.next = self.head

        # If linked list is not None then set the next of
        # last node
        if self.head is not None:
            while (temp.next != self.head):
                temp = temp.next
            temp.next = ptr1

        else:
            ptr1.next = ptr1  # For the first node

        self.head = ptr1

    # Function to print nodes in a given circular linked list
    def printList(self):
        temp = self.head
        if self.head is not None:
            while (True):
                print("%d" % (temp.data))
                temp = temp.next
                if (temp == self.head):
                    break

    # Function to split a list (starting with head) into
    # two lists. head1 and head2 are the head nodes of the
    # two resultant linked lists
    def splitList(self, head1, head2):
        #main linked list is self.head
        count = 0
        temp = self.head
        print("original ll")
        while(temp.next!=self.head):
            count =count+1
            temp = temp.next
        count = count+1
        mid = int(math.ceil(count / 2))
        print("count is",count,"and mid is",mid)
        temp1 = self.head
        while(mid-1):
            temp1 = temp1.next
            mid = mid -1
        print("pointer is at",temp1.data)
        nextpointer = temp1.next
        temp1.next = self.head
        head1.head = self.head
        head2.head = nextpointer
        while(nextpointer.next!=self.head):
            nextpointer = nextpointer.next
        nextpointer.next = head2.head


# Initialize lists as empty
head = CircularLinkedList()
head1 = CircularLinkedList()
head2 = CircularLinkedList()

head.push(12)
head.push(56)
head.push(2)
head.push(11)

print("Original Circular Linked List")
head.printList()

# Split the list
head.splitList(head1, head2)

print("\nFirst Circular Linked List")
head1.printList()

print("\nSecond Circular Linked List")
head2.printList()


