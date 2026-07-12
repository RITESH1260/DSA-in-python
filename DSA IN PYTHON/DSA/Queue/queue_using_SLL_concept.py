from singly_linked_list import SLL

class queue:
    def __init__(self):
        self.mylist = SLL()
        self.item_count = 0
        self.front = None
        self.rear = None
    def is_empty(self):
        return self.mylist.is_empty()
    
    def enqueue(self, data):
        self.mylist.insert_at_last(data)
        self.item_count += 1
        if self.front is None:
            self.front = self.mylist.start
        self.front = self.mylist.start
        temp = self.mylist.start
        while temp.next is not None:
            temp = temp.next
        self.rear = temp
            
    def dequeue(self):
        if not self.is_empty():
            data = self.mylist.start.item
            self.mylist.delete_first()
            self.item_count -= 1
            if self.item_count == 0:
                self.front = None
                self.rear = None
            return data
        else:
            raise IndexError("Queue is empty, cannot dequeue.")
    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            raise IndexError("Queue is empty, cannot get front element.")
    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        else:
            raise IndexError("Queue is empty, cannot get rear element.")
    def size(self):
        return self.item_count
    
s1 = queue()
s1.enqueue(10)
s1.enqueue(20)  
s1.enqueue(30)
s1.enqueue(40)
print("The front element is:", s1.get_front())  # Output: 10
print("The rear element is:", s1.get_rear())   # Output: 40
print("The size of the queue is:", s1.size())      # Output: 4