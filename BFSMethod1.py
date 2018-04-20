#class that represent individual node in binary tree
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

#function for level order tree traversal
def printLevelOrder(tree):
    h = height(tree)
    for i in range(1,h+1):
        printGivenLevel(tree,i)

#function to print node of given level 
def printGivenLevel(root,level):
    if root is None:
        return
    if level == 1:
        print "%d" %(root.data),
    elif level > 1:
        printGivenLevel(root.left,level-1)
        printGivenLevel(root.right,level-1)

#calculate height of tree
def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)
        if lheight>rheight:
            return lheight+1
        else:
            return rheight+1


#driver program
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print "here is level order tree traversal of binary tree"
printLevelOrderTraversal(root)
