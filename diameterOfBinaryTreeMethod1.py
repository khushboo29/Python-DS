#diameter of binary tree in python by recursion in time complexity O(n raise to power 2)
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key
        
#function to calculate height of tree
def height(root):
    if root is None:
        return 0
#if tree is not null then height is 1+max of left tree height,right tree height
    return 1+max(height(root.left),height(root.right))

#function to get diameter of binary tree
def diameter(root):
    if root is None:
        return 0;
    lheight = height(root.left)
    rheight = height(root.right)
    ldiameter = diameter(root.left)
    rdiameter = diameter(root.right)
#diameter of binary tree is equal to max of following
#1)diameter of left tree
#2)diameter of right tree
#3)height of left tree + height of right tree + 1
    return(max(lheight+rheight+1,max(ldiameter,rdiameter)))
    
#driver code 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print "Diameter of given binary tree is %d" %(diameter(root))

