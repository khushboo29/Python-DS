# Python program for diagonal traversal of Binary Tree
#d = diagonal distance 
#There are two rules for find d 
#for left child d should be  d = d+10
#for right child d should be same as parent d = d of parent

# A binary tree node
class Node:

	# Constructor to create a new binary tree node
	def __init__(self, data):
		self.data = data 
		self.left = None
		self.right = None

def diagonalPrintUtil(root, d, diagonalPrintMap):
	
	# Base Case 
	if root is None:
		return

	# Store all nodes of same line together as a vector
	try :
		diagonalPrintMap[d].append(root.data)
	except KeyError:
		diagonalPrintMap[d] = [root.data]

	# Increase the vertical distance if left child
	diagonalPrintUtil(root.left, d+1, diagonalPrintMap)
	
	# Vertical distance remains same for right child
	diagonalPrintUtil(root.right, d, diagonalPrintMap)



# Print diagonal traversal of given binary tree
def diagonalPrint(root):

	# Create a dict to store diagnoal elements 
	diagonalPrintMap = dict()
	
	# Find the diagonal traversal
	diagonalPrintUtil(root, 0, diagonalPrintMap)

	print "Diagonal Traversal of binary tree : "
	for i in diagonalPrintMap:
		for j in diagonalPrintMap[i]:
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

diagonalPrint(root)

