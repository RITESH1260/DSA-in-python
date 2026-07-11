class queue:
    
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return len(self.items) == 0
    def enqueue(self, data):
        return self.items.append(data)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty, cannot dequeue.")
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty, cannot get front.")
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Queue is empty, cannot get rear.")
    def size(self):
        return len(self.items)
    
s1 = queue()
s1.enqueue(10)
s1.enqueue(20)
s1.enqueue(30)
try:
    print(s1.dequeue())  # Output: 10
except IndexError as e:
    print(e)
print(s1.get_front())  # Output: 10
print(s1.get_rear())   # Output: 30     
        