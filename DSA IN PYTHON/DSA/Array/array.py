#Array is not a built-in data structure and therfore need to be imported.

from array import *
a1 =array('i', [5,10,15,20,25])
for x in a1:
    print(x)
    
for x in range(len(a1)):
    print(a1[x])
    
#Array methods

a1.append(30)  # Add an element at the end
a1.insert(2,12)  # Insert an element at a specific index
a1.extend([35,40,45])  # Add multiple elements at the end
a1.remove(20)  # Remove the first occurrence of an element  
a1.pop(3)  # Remove an element at a specific index
a1.index(15)  # Get the index of the first occurrence of an element
a1.reverse()  # Reverse the order of elements
a1.buffer_info()  # Get the memory address and size of the array