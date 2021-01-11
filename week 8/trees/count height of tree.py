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
def heightOfTree(root1):
    if root1 == None:
        return 0
    else:
        leftHieght = heightOfTree(root1.left)
        rightHieght = heightOfTree(root1.right)
        return max(leftHieght,rightHieght) + 1


#
#         1
#       /   \
#     2       3
#   /  \       \
# 4     5       6
# # Driver code
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
printLevelOrder(root)
print("\nheight of tree is ",heightOfTree(root))