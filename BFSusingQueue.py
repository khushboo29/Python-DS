#traversal of binary tree in python
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key

#function to print level order traversal by using queue
def printLevelOfOrderByQueue(root):
    if root is None:
        return 
    queue = []
    queue.append(root)
    while(len(queue) > 0):
        print queue[0].data,
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
     
#driver code 
root = Node(1)
root.left= Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)

print "Preorder traversal of binary tree is"
printLevelOfOrderByQueue(root)

