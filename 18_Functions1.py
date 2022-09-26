def greet():
    print("Hello")
    print("Good Morning")

greet()

def add(x,y):
    c = x+y
    return c

greet()
result = add(5,4)
print(result)

def add_sub(x,y):
    c = x+y
    d = x-y
    return c,d

result1,result2 = add_sub(5,4)
print(result1, result2)

def update(x):

    print(id(x))

    x = 8
    print(id(x))
    print("x ", x)

a = 10
print(id(a))
update(a)
print("a ", a)

def update(lst):

    print(id(lst))

    lst[1] = 25
    print(id(lst))
    print("x ", lst)

lst = [10,20,30]
print(id(lst))
update(lst)
print("lst ", lst)