a=10
b=10
print(id(a))
print(id(b))
print(id(10))

num = b
print(id(num))
print(id(b))

b=5
print(id(b))
print(id(num))

PI = 3.14
print(type(PI))
