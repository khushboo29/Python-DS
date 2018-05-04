#print vertical level of binary try:
#we need to calculate Horizontal Distance for this 
#for root hd= 0 
#for left hd= hd-1
#for right hd= hd+1

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printVerticalUtils(root,d,printMap):
    if root is None:
        return
    try:
        printMap[d].append(root.data)
    except KeyError:
        printMap[d] = [root.data]
    printVerticalUtils(root.left,d-1,printMap)
    printVerticalUtils(root.right,d+1,printMap)

def printVertical(root):
    printMap = dict()
    printVerticalUtils(root,0,printMap)
    for i in printMap:
        for j in printMap[i]:
            print j,
        print ""
 
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
 
printVertical(root)           
    
