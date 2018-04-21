#diameter of binary tree in python by Optimize finding diameter of binary tree in time complexity O(n)
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key
        
#function to calculate diameter of tree
def find_tree_diameter(root):
    if root is None:
        return 0
    d,_ = diameter_height(root)
    return d

#function to get diameter_height of binary tree for each node at one iteration
#Python supports multiple return values
def diameter_height(root):
    if root is None:
        return 0,0;
    ldiameter,lheight = diameter_height(root.left)
    rdiameter,rheight = diameter_height(root.right)
    return max(lheight+rheight+1,ldiameter,rdiameter),max(lheight,rheight)+1
    
#driver code 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print "Diameter of given binary tree is %d" %(find_tree_diameter(root))

