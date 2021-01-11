
def printPreorder(root1):
    if root1==None:
        return
    print(root1.val, end=" ")
    printPreorder(root1.left)
    printInorder(root1.right)
    return
def printInorder(root1):
    if root1==None:
        return
    printInorder(root1.left)
    print(root1.val, end=" ")
    printInorder(root1.right)
    return
def printPostorder(root1):
    if root1==None:
        return
    printPostorder(root1.left)
    printInorder(root1.right)
    print(root1.val, end=" ")
    return
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
def insertingNode(root1,key):
    if root1 == None:
        return
    queue = []
    tmp = Node(key)
    queue.append(root1)
    while(len(queue)!=0):
        current_pounter = queue[0]
        if current_pounter.left == None:
            current_pounter.left=tmp
            return
        if current_pounter.right == None:
            current_pounter.right = tmp
            return
        if current_pounter.left != None:
            queue.append(current_pounter.left)
        if current_pounter.right != None:
            queue.append(current_pounter.right)
        queue.pop(0)

    return

def delANode(root1,key):
    #if root is the only node
    if root1.left == None and root1.right == None:
        if root1.val == key:
            root1 = None
            return
        else:
            return -1
    else:
        # key is at leaf node
        queue = []
        tmp = Node(key)
        queue.append(root1)
        while (len(queue) != 0):
            current_pounter = queue[0]
            if current_pounter.val == 12:
                if current_pounter.left == None and current_pounter.right == None:
                    #delete the link from
                    #what to do
                    pass
            if current_pounter.left != None:
                queue.append(current_pounter.left)
            if current_pounter.right != None:
                queue.append(current_pounter.right)

            queue.pop(0)
        pass
    return


def count_Nodes_with_No_Sibling(root1,lst):
    if root1 == None:
        return 0
    # print(root1.val)
    #condion for no sibling
    if (root1.left == None and root1.right!=None):
        print("\nnode having no siblings",root1.right.val)
        lst.append(root1.right.val)
        # return 1
    if root1.right == None and root1.left!=None:
        print("\nnode having no siblings",root1.left.val)
        lst.append(root1.left.val)
        # return 1
    if root1.left!=None or root1.right!=None:
        in_left = count_Nodes_with_No_Sibling(root1.left,lst)
        in_right = count_Nodes_with_No_Sibling(root1.right,lst)
        return
    return
#
# #
#         1
#      /    \
#     2       3
#      \     /
#       4   5
#          /
#         6
# # Driver code
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

root = Node(1)
root.left  = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.left.left= Node(6)

print ("Preorder traversal of binary tree is")
printPreorder(root)

print("\nInorder traversal of binary tree is")
printInorder(root)

print("\nPostorder traversal of binary tree is")
printPostorder(root)

print("\nLevel Order Travesel of binary tree is")
printLevelOrder(root)

#for inserting a node in bt
# insertingNode(root,12)

print("\nafter inserting level order travesring is")
printLevelOrder(root)
delANode(root,12)
print("\nafter deleting 12 from tree")
printLevelOrder(root)
count_lst = []
print("\ncount",count_Nodes_with_No_Sibling(root,count_lst))
print(count_lst)