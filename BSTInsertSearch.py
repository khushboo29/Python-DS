#BST binary search tree where left node is less than root and right node is greater than root.
#search a key in BST
#insert a node in BST
class Node:
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None

def search(root,key):
    if root is None or root.val == key:
        return root
    if(key < root.val):
        return search(root.left,key)
    elif(key > root.val):
        return search(root.right,key)

def insert(root,node):
    if root is None:
       root = node
    else:
        if(node.val < root.val):
            if root.left is None:
                root.left = node
            else:
                insert(root.left,node)
        elif(node.val > root.val):
            if root.right is None:
                root.right = node
            else:
                insert(root.right,node)

def inorder(root):
    if root is None:
        return
    else:
        inorder(root.left)
        print(root.val),
        inorder(root.right)

r = Node(50)
insert(r,Node(30))
insert(r,Node(20))
insert(r,Node(40))
insert(r,Node(70))
insert(r,Node(60))
insert(r,Node(80))
inorder(r)
