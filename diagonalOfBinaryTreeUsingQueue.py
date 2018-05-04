# Python program for diagonal traversal of Binary Tree
#using queue

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def diagonalPrint(root):
    q = []
    q.append(root)
    q.append(None)
    
    while(len(q)>0):
        p = q.pop(0)
        if p is None:
            q.append(None)
            p = q.pop(0)
            if p is None:
                break;
        if p is not None:
            print p.data,
            q.append(p.left)
            p = p.right
    

# Driver Program 
root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)
root.right.right.left = Node(13)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
diagonalPrint(root)
