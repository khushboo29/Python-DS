#delete node from bst
class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

def insert(node,key):
    if node is None:
       return Node(key)
    else:
        if key < node.key:
            node.left = insert(node.left,key)
        else:
            node.right = insert(node.right,key)
    return node

def deleteNode(root,key):
    if root is None:
        return root
    if(key < root.key):
        root.left = deleteNode(root.left,key)
    elif( key > root.key):
        root.right = deleteNode(roo.right,key)
    else:
#for one child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
#for two child
# Node with two children: Get the inorder successor
# (smallest in the right subtree)
        temp = minValueNode(root.right)
        root.val = temp.val
        root.right = deleteNode(root.right,temp.key)

def minValueNode(node):
    current = node
    if node.left is not None:
        current = current.left
    return current

def inorder(root):
    if root is None:
        return
    else:
        inorder(root.left)
        print(root.key),
        inorder(root.right)

root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print("Inorder traversal of the given tree")
inorder(root)

print("\nDelete 20")
root = deleteNode(root, 20)
print("Inorder traversal of the modified tree")
inorder(root)

print ("\nDelete 30")
root = deleteNode(root, 30)
print( "Inorder traversal of the modified tree")
inorder(root)

print ("\nDelete 50")
root = deleteNode(root, 50)
print ("Inorder traversal of the modified tree")
inorder(root)
