class Node:
    def __init__(self, item = None, prev = None, next = None):
        self.prev = prev
        self.item = item
        self.next = next
        
class deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0
    
    def is_empty(self):
        return self.front ==None
        return self.item_count == 0
    
    def insert_front(self, data):
        n = Node(data, None, self.front)
        if self.is_empty():
            
            self.rear = n
        else:
            self.front.prev = n
            
        self.front = n 
        self.item_count += 1  
    
    def insert_rear(self, data):
        n = Node(data,self.rear , None)
        if self.is_empty():
            self.front = n
        else:
            self.rear.next = n
        self.rear = n
        self.item_count += 1
        
    def delete_front(self):
        if self.is_empty():
            raise IndexError("deque is empty")
        if self.front ==self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.item_count -= 1
            
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("DEQUE IS EMPTY")
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self.item_count -= 1
    
    def get_front(self):
        if self.is_empty():
            raise IndexError("deque is empty")
        return self.front.item
    
    def get_rear(self):
        if self.is_empty():
            raise IndexError("deque is empty")
        return self.rear.item
    
    def size(self):
        return self.item_count
    
d1 = deque()
d1.insert_front(10)
d1.insert_rear(50)
d1.insert_front(5)
print("The front element is:",d1.get_front())
print("The rear element is:",d1.get_rear())
print("The size of the node is:", d1.size())