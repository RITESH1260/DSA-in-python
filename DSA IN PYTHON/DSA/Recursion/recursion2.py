def sum(n):
    if n == 0:
        return 0
    return n + sum(n-1)


def sumodd(n):
    if n == 0:
        return 0
    return 2*n-1 + sumodd(n-1)
# print("sum is",sumodd(5))
def sumeven(n):
    if n == 0:
        return 0
    return 2*n + sumeven(n-1)

def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

def sumofsquare(n):
    if n == 1:
        return 1
    return n*n + sumofsquare(n-1)

print("sum is",sumofsquare(5))


               