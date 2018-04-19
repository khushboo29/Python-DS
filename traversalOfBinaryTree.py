#traversal of binary tree in python
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

#function to print inorder traversal
def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val),
        printInorder(root.right)
    
def printPreorder(root):
    if root:
        print(root.val),
        printPreorder(root.left)
        printPreorder(root.right)

def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val),
        
#driver code 
root = Node(1)
root.left= Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)

print "Preorder traversal of binary tree is"
printPreorder(root)
 
print "\nInorder traversal of binary tree is"
printInorder(root)
 
print "\nPostorder traversal of binary tree is"
printPostorder(root)
