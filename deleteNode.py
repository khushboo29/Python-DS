class Node:
    def __init__(self,data):
        self.data = data
        self.right = self.left = None
        
#function to delete node from binary tree        
def deleteTree(node):
    if node is None:
        return 0
    deleteTree(node.left)
    deleteTree(node.right)
    node.left = None
    node.right = None

#preorder traversal with recursion
def traverse(node):
    if node is None:
        return 0
    print node.data,
    traverse(node.left)
    traverse(node.right)

#driver code
node  = Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.left = Node(4)
node.left.right = Node(5)
print "your tree is .."
traverse(node)
print "\n you are deleting tree..."
deleteTree(node)

