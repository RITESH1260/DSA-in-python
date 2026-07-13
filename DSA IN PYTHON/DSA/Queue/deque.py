class deque:
    
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return len(self.items) == 0
    
    def insert_front(self, data):
        self.items.insert(0, data)
        
    def insert_rear(self, data):
        self.items.append(data)
        
    def delete_front(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise IndexError("Deque is empty. Cannot delete from front.")
    def delete_rear(self):
        if not self.is_empty():
            self.items.pop()
        else:
            raise IndexError("Deque is empty. Cannot delete from rear.")
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Deque is empty. Cannot get front element.")
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Deque is empty. Cannot get rear element.")
        
    def size(self):
        return len(self.items)
    
d1 = deque()
d1.insert_front(10)
d1.insert_rear(20)
d1.insert_front(5)
print("Front element:", d1.get_front())  # Output: 5
print("Rear element:", d1.get_rear())    # Output: 20
print("Size of deque:", d1.size())        # Output: 3
print("Deleting front element...")
d1.delete_front()
print("Front element after deletion:", d1.get_front())  # Output: 10