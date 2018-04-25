class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None
        
def countLeaves(node):
    if node is None:
        return 0
    if(node.left is None and node.right is None):
        return 1
    else:
        return (countLeaves(node.left) + countLeaves(node.right) )
    
def traverse(node):
    if node is None:
        return 0
    print node.data
    traverse(node.left)
    traverse(node.right)

def deleteNode(node,X):
    if node is None:
        #countLeaves(node)
        return
    if node.data == X:
        node.left = None
        node.right = None
        node.data = None
        countLeaves(node)
    else:
        deleteNode(node.left,X)
        deleteNode(node.right,X)
        return 1

def createNode(parent,i,created,root):
    if created[i] is not None:
        return
    created[i] = Node(i)
    if parent[i] == -1:
        root[0] = created[i]
        return
    if created[parent[i]] is None:
        createNode(parent,parent[i],created,root)
        
    p = created[parent[i]]
    #print p.data
    if p.left is None:
        p.left = created[i]
        #print p.left.data
    else: 
        p.right = created[i]
        #print p.right.data
        
def createTree(parent):
    n = len(parent)
    #print n
#initialize array to keep track of created nodes
    created = [None for i in range(n+1)]
    root = [None]
    #print root
    #print created
    for i in range(n):
        createNode(parent,i,created,root)
        
    return root[0]
