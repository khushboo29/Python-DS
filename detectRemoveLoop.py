class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None;
        
    def detectLoop(self):
        s = p = self.head;
        while (s and p and p.next):
            s = s.next
            p = p.next.next
        
            if s == p:
                self.removeLoop(s)
                return 1 
        return 0
        
    def removeLoop(self,loop_node):
        i = self.head;
        while(1):
            j = loop_node;
            while(j.next != loop_node and j.next != i):
                j = j.next
                
            if j.next == i :
                break
            i = i.next
        j.next = None
        
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def printList(self):
        temp = self.head
        while(temp):
            print temp.data,
            temp = temp.next
# Driver program
llist = LinkedList()
llist.push(10)
llist.push(4)
llist.push(15)
llist.push(20)
llist.push(50)

# Create a loop for testing
llist.head.next.next.next.next.next = llist.head.next.next

llist.detectLoop()
 
print "Linked List after removing loop"
llist.printList()
