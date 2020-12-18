# User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

def getlen(head):
    count=0
    while(head!=None):
        count+=1
        head = head.next
    return count
def deleteMid(head):
    tmp = head
    len1 = getlen(head)
    if len1 == 0:
        return None
    if len1 == 1:
        return None
    if len1 == 2:
        print("len is two")
        head.next = None
        return head
    posToBeDelete = len1 // 2 + 1
    # print(posToBeDelete)
    prev = head
    while(posToBeDelete):
        posToBeDelete = posToBeDelete - 1
        prev = tmp
        tmp = tmp.next
    # print(prev.data)
    prev.data = prev.next.data
    prev.next = prev.next.next
    return head

    # code here

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


def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):
        n = int(input())
        arr1 = [int(x) for x in input().split()]
        ll = Llist()
        tail = None
        for nodeData in arr1:
            tail = ll.insert(nodeData, tail)

        res = deleteMid(ll.head)
        printList(res)
# } Driver Code Ends