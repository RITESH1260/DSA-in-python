from singly_linked_list import *

class stack(SLL):
    def __init__ (self): #__init__ method is used to initialize the stack object
        
        super().__init__()  #super() is used to call the constructor of the parent class SLL
        
        self.item_count = 0
    def is_empty(self):
        return super().is_empty()
    def push(self, data):
        self.insert_at_start(data)
        self.item_count += 1
    def pop(self):
        if not self.is_empty():
            self.delete_first()
            self.item_count -= 1
        else:
            raise IndexError("Stack is empty, cannot pop.")
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Stack is empty, cannot peek.")
    def size(self):
        return self.item_count
    
s1 = stack()
s1.push(10)
s1.push(20)
s1.push(30)
print(s1.peek())  # Output: 30
print(s1.size())  # Output: 3
s1.pop()
print(s1.peek())  # Output: 20
print(s1.size())  # Output: 2
        
        
    