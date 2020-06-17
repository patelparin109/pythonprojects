# Lambda Function or Anonymous Function

def add(a,b):
    return a + b
add = lambda x, y : x + y

minus = lambda x, y : x - y

def minus(x,y):
    return x - y

print(add(9,4))
print(minus(9,4))

def a_first(a):
    return a[1]

a = [[1, 14], [9, 6], [8,23]]
a.sort(key=lambda x:x[1])
print(a)