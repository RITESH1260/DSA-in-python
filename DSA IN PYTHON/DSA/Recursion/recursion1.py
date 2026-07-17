#1. write a recursive function to print first N natural numbers.

'''def f1(N):
    if N==1:
        return 1
    s = N + f1(N-1)
    return s

r = f1(10)
print(r)
    
#2. write a recursive function to print first N natural numbers in reverse order.
def f1(n):
    
    if n == 0:
        return 
    print(2 * n - 1)
    f1(n - 1)
    
f1(10)

#3. write a recursive function to print first N odd natural numbers.
def f(n):
    if n == 0:
        return
    f(n-1)
    print(2 * n - 1)
r = f(10)

#4. write a recursive function to print first N even natural numbers.
def f(n):
    if n == 0:
        return
    f(n-1)
    print(2*n)

f(9)

#5. write a recursive function to print first N odd natural numbers in reverse order.
def f(n):
    if n == 0:
        return
    
    print(2 * n - 1)
    f(n-1)
f(10)

#5. write a recursive function to print first N even natural numbers in reverse order.
def f(n):
    if n == 0:
        return
    
    print(2*n)
    f(n-1)
f(10)'''
def f(n):
    if n > 0 :
        f(n - 1)
        print(n, end = ' ')
f(10)

def f1(n):
    if n > 0 :
        print(n, end = ' ')
        f1(n - 1)
        
f1(10)
def f1(n):
    if n > 0 :
        f1(n - 1)
        print(2*n-1, end = ' ')
        
f1(10)
def f1(n):
    if n > 0 :
        f1(n - 1)
        print(2*n, end = ' ')
        
f1(10)
    
        
        
        

    