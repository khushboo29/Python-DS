#write ENQUEUE and DEQUEUE to detect underflow and overflow of a queue

class Queue:
    def __init__(self,max_size=0):
        self.size = max_size
        self.items = []
        
    def isEmpty(self):
        return len(self.items)==0
    
    def isFull(self):
        return len(self.items) == self.size
        
    def EnQueue(self,item):
        if self.isFull():
            print("queue is full")
            return
        else:
            self.items.append(item)
            print("%s enqueued to queue"  %str(item))
            
    def DeQueue(self):
        if self.isEmpty():
            print("queue is empty")
            return
        x = self.items.pop(0)
        print("%s dequeued to queue" %str(x))
            
    def front_head(self):
        if self.isEmpty():
            print("empty queue")
            return
        else:
            print("front_head item is: ", self.items[0])
        
    def rear_tail(self):
        if self.isFull():
            print("full queue")
            return
        else:
            print("rear_tail item is:", (self.items[len(self.items)-1]))

# Driver Code
#if __name__ == '__main__':
queue = Queue(30)
queue.EnQueue(10)
queue.EnQueue(20)
queue.EnQueue(30)
queue.EnQueue(40)
queue.DeQueue()
queue.front_head()
queue.rear_tail()
        
