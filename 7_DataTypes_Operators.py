import math

a=5
print("Type of a: ", type(a))

b=5.0
print("Type of b: ", type(b))

c = 2+4j
print("Type of c: ", type(c))

String1 = "Welcome to the programming world"
print(String1)

String2 = '''Shivay
             is 
             a
             good boy.'''
print(String2)

print(String2[2])
print(String1[-1])

List = ['Shivay', 'Sabharwal']
print(List[0])

Tuple1 = ('A', 'B', 1.8, 66)
print(Tuple1)
print(Tuple1[-3])

print(type(True))
print(int(False))

set1 = {1,66,8.0,7}
print(set1)

Dict1 = {1:'Shivay', 2:'Pranav', 3:'Satvik'}
print(Dict1[1])

a = 9
b = 6

add = a+b
sub = a-b
mul = a*b
div1 = a/b
div2 = a//b
mod = a%b
p = a**b

print(add)
print(sub)
print(mul)
print(div1)
print(div2)
print(mod)
print(p)

a = 13
b = 33

# a > b is False
print(a > b)

# a < b is True
print(a < b)

# a == b is False
print(a == b)

# a != b is True
print(a != b)

# a >= b is False
print(a >= b)

# a <= b is True
print(a <= b)

# Examples of Logical Operator
a = True
b = False

# Print a and b is False
print(a and b)

# Print a or b is True
print(a or b)

# Print not a is False
print(not a)

# Examples of Bitwise operators
a = 10
b = 4

# Print bitwise AND operation
print(a & b)

# Print bitwise OR operation
print(a | b)

# Print bitwise NOT operation
print(~a)

# print bitwise XOR operation
print(a ^ b)

# print bitwise right shift operation
print(a >> 2)

# print bitwise left shift operation
print(a << 2)

# Examples of Assignment Operators
a = 10

# Assign value
b = a
print(b)

# Add and assign value
b += a
print(b)

# Subtract and assign value
b -= a
print(b)

# multiply and assign
b *= a
print(b)

# bitwise lishift operator
b <<= a
print(b)

a = 10
b = 20
c = a

print(a is not b)
print(a is c)

# Python program to illustrate
# not 'in' operator
x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")

# Examples of Operator Precedence

# Precedence of '+' & '*'
expr = 10 + 20 * 30
print(expr)

# Precedence of 'or' & 'and'
name = "Alex"
age = 0

if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome.")
else:
    print("Good Bye!!")

# Examples of Operator Associativity

# Left-right associativity
# 100 / 10 * 10 is calculated as
# (100 / 10) * 10 and not
# as 100 / (10 * 10)
print(100 / 10 * 10)

# Left-right associativity
# 5 - 2 + 3 is calculated as
# (5 - 2) + 3 and not
# as 5 - (2 + 3)
print(5 - 2 + 3)

# left-right associativity
print(5 - (2 + 3))

# right-left associativity
# 2 ** 3 ** 2 is calculated as
# 2 ** (3 ** 2) and not
# as (2 ** 3) ** 2
print(2 ** 3 ** 2)

### Number System Conversion
print(bin(20))
print(hex(23))
print(oct(44))

### SWapping Numbers
a = 40
b = 50

a,b = b,a

temp = a
a = b
b = temp
print(a)
print(b)

a = a+b
b = a-b
a = a-b
print(a)
print(b)

a = a^b
b = a^b
a = a^b
print(a)
print(b)

### BITWISE OPERATORS
print(~12)
print(12&13)
print(12|14)
print(12^13)
print(10<<12)

print(math.floor(5.4))
print(math.ceil(5.2))
print(math.pow(2,5))

print(math.pi)
print(math.e)

print(help('math'))