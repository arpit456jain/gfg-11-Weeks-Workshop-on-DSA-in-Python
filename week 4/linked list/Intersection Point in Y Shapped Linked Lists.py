# User function Template for python3
'''
	Function to return the value at point of intersection
	in two linked list, connected in y shaped form.

	Function Arguments: head_a, head_b (heads of both the lists)

	Return Type: value in NODE present at the point of intersection
	             or -1 if no common point.

	Contributed By: Arpit Jain  

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''


def intersetPoint(head1, head2):
    lst = []
    while(head1!=None):
        lst.append(head1)
        head1=head1.next
    while(head2!=None):
        if head2 in lst:
            return head2.data
        head2 = head2.next
    return -1

def intersetPoint2(head1, head2):
    c1=0
    tmp1 = head1
    tmp2 = head2
    while(head1!=None):
        c1=c1+1
        head1 = head1.next
    c2=0
    while(head2!=None):
        c2 = c2 +1
        head2 = head2.next

    head1  = tmp1
    head2 = tmp2
    if c1 == c2:
        while(head1!=None and head2!=None):
            if head1 == head2:
                return head2.data
            head2=head2.next
            head1=head1.next
    elif c1>c2 :
        d  = c1 - c2
        while(d):
            head1 = head1.next
            d=d-1
        while (head1!= None):
            if head2 == head1:
                return head1.data
            head2 = head2.next
            head1 = head1.next
        return head2.data
    elif c2 > c1:
        need = c2 -c1
        # print(need)
        while(need):
            head2 = head2.next
            need = need - 1
        while(head2!=None):
            if head2 == head1:
                return head2.data
            head2 = head2.next
            head1 = head1.next
        return head2.data

    return -1

# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        temp = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            self.temp = self.head
            return
        else:
            self.temp.next = new_node
            self.temp = self.temp.next


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        x, y, z = map(int, input().strip().split())
        a = LinkedList()  # create a new linked list 'a'.
        b = LinkedList()  # create a new linked list 'b'.
        nodes_a = list(map(int, input().strip().split()))
        nodes_b = list(map(int, input().strip().split()))
        nodes_common = list(map(int, input().strip().split()))

        for x in nodes_a:
            node = Node(x)
            a.append(node)  # add to the end of the list

        for x in nodes_b:
            node = Node(x)
            b.append(node)  # add to the end of the list

        for i in range(len(nodes_common)):
            node = Node(nodes_common[i])
            a.append(node)  # add to the end of the list a
            if i == 0:
                b.append(node)  # add to the end of the list b, only the intersection

        print(intersetPoint2(a.head, b.head))

