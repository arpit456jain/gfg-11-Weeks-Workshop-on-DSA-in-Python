'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''


def printInorder(root1):
    if root1==None:
        return
    printInorder(root1.left)
    print(root1.data, end=" ")
    printInorder(root1.right)
    return
def makeMirrorTree(root1):
    if root1 == None:
        return
    else:
        #swap the left and right node
        tmpNode = root1.left
        root1.left = root1.right
        root1.right = tmpNode
        makeMirrorTree(root1.left)
        makeMirrorTree(root1.right)
def checkMirror(root1,root2):
    if root1 == None or root2 == None:
        return
    else:
        if root1.data == root2.data:
            if(checkMirror(root1.left,root2.left) == -1):
                return -1
            if(checkMirror(root1.right,root2.right) == -1):
                return -1
        else:
            return -1

def areMirror(root1, root2):
    makeMirrorTree(root1)
    #chlo maine upr wale functions se mirror tree bna bhi liya to
    #check kaise kru ki same hai
    flag=checkMirror(root1,root2)
    if flag == -1:
        return False
        # print("not mirror")
    else:
        return True
        # print("mirror")

from collections import deque


# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        str1 = input()
        str2 = input()
        root1 = buildTree(str1)
        root2 = buildTree(str2)
        if areMirror(root1, root2) == True:
            print(1)
        else:
            print(0)

# } Driver Code Ends