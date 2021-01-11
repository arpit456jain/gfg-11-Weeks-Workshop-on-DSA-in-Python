# User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''


# your task is to complete this function
# function should return the count of Leaf node's
# Note: You required to print a new line after every test case
def countLeaves(root1):
    #shi khel gya code pass ho gya yr
    if root1==None:
        return 0
    elif root1.left == None and root1.right == None:
        return 0
    else:
        counter = 0
        queue = []
        queue.append(root1)
        while(len(queue)!=0):
            current_pounter = queue[0]

            #let me check if both child are absent or not
            if current_pounter.left == None and current_pounter.right == None:
                counter+=1
            if current_pounter.left!=None:
                queue.append(current_pounter.left)
            if current_pounter.right!=None:
                queue.append(current_pounter.right)
            queue.pop(0)

        return counter

def countLeafByRecursion(root1):
    if root1 == None:
        return 0
    if root1.left == None and root1.right == None:
        return 1
    else:
        leafInLeft = countLeafByRecursion(root1.left)
        leafInright = countLeafByRecursion(root1.right)
        return  leafInLeft + leafInright

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


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        print(countLeaves(root))
        print("by recursion",countLeafByRecursion(root))


# } Driver Code Ends