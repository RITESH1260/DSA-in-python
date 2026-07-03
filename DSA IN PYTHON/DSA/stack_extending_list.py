'''class stack:
    class list:
        def __init__(self):
            self.item = []
        def is_empty(self):
            return len(self.item) == 0
        def push(self, data):
            self.item.append(data)
        def pop(self):
            if not self.is_empty():
                return self.item.pop()
            else:
                raise IndexError("stack is empty")
        def peek(self):
            if not self.is_empty():
                return self.item[-1]
            else:
                raise IndexError("stack is empty")
        def size(self):
            return len(self.item)
        def insert(self, data):
            self.item.append(data)
s1=stack.list()
s1.push(10)
s1.push(20)
s1.push(30)
print("Top element is:",s1.peek())
s1.insert(50)
print("Inserted element is:",s1.insert(40))
print("Stack size is:",s1.size())'''

class stack(list):
    def is_empty(self):
        return len(self) == 0
    def push(self, data):
        self.append(data)
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("stack is empty")
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("stack is empty")
    def size(self):
        return len(self)
    def insert(self,index,data):
        raise AttributeError("'insert' method is not supported in stack")
s1=stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("Top element is:",s1.peek())
s1.insert(1,50)
    
            