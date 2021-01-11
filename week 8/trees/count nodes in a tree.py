def printLevelOrder(root1):
    if root1==None:
        return
    queue = []
    queue.append(root1)
    while(len(queue)!=0):
        current_pounter = queue[0]

        if current_pounter.left!=None:
            queue.append(current_pounter.left)
        if current_pounter.right!=None:
            queue.append(current_pounter.right)
        print(current_pounter.val, end=" ")
        queue.pop(0)

    return
def countNodes(root1):
    if root1==None:
        return 0
    elif root1.left == None and root1.right == None:
        return 1
    else:
        counter = 0
        queue = []
        queue.append(root1)
        while(len(queue)!=0):
            current_pounter = queue[0]

            if current_pounter.left!=None:
                queue.append(current_pounter.left)
            if current_pounter.right!=None:
                queue.append(current_pounter.right)
            queue.pop(0)
            counter+=1

        return counter

def countNodesByRecursion(root1):
    if root1 == None:
        return 0
    else:
        leftcount = countNodesByRecursion(root1.left)
        rightcount = countNodesByRecursion(root1.right)
        total = leftcount + rightcount + 1
        return total
#
#         1
#       /   \
#     2       3
#   /   \      \
# 4      5      6
# # Driver code
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

root = Node(1)
root.left  = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right= Node(6)

print("\nLevel Order Travesel of binary tree is")
printLevelOrder(root)
print("\nno of nodes in tree by use of level traversing",countNodes(root),end=" ")
print("\nno of nodes by recursion ",countNodesByRecursion(root))
print("\nLevel Order Travesel of binary tree is")
printLevelOrder(root)