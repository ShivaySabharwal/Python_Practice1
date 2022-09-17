# the key should be of immutable type always
data = {1:"Shivay", 2:"Pranav", 5:"Satvik"}
print(data)

print(data[1])

print(data.get(5))

print(data.get(3,"Not Applicable"))
print(data.get(2,"Not Applicable"))

keys = {"Shivay", "Pranav", "Satvik"}
values = {"Python", "C++", "ABC"}
data1 = dict(zip(keys,values))
print(data1)

del data1["Shivay"]
print(data1)

data2 = {'js':'Atom', 'cs':'vs', 'Python':[11,22,33]}
print(data2['Python'][2])