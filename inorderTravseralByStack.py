#function to traverse tree by inorder traversal without recursion 
#but using stack
class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
        

#inorder traversal without recursion but using stack
def traverse(root):
    done = 0
    s = []
    cur = root
    while(not done):
        if cur is not None:
            s.append(cur)
            cur = cur.left
        else:
            if (len(s)>0):
                cur =  s.pop()
                print cur.data,
                cur = cur.right
            else:
                done=1

#driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print "your tree is .."
traverse(root)


