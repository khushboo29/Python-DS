#reverse order level travsersal

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printGivenLevel(root,level):
    if root is None:
        return
    if level ==1:
        print root.data,
    elif level>1:
        printGivenLevel(root.left,level-1)
        printGivenLevel(root.right,level-1)
        
def reverseLevelOrder(root):
    h = height(root)
    for i in reversed(range(1, h+1)):
        printGivenLevel(root,i)
        

def height(root):
    if root is None:
        return 0
    else:
        lheight = height(root.left)
        rheight = height(root.right)
        if lheight > rheight:
            return lheight+1 
        else:
            return rheight+1

# Driver pogram to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
 
print "reverse Order traversal of binary tree is"
reverseLevelOrder(root)
