f = open('MyData','r')
print(f.read())
print(f.readline(4),end="")

f1 = open('abc','a')
f1.write("Something")
f1.write("People")
f1.write('Mobile')


f = open('MyData','r')

f1 = open('abc','w')

for data in f:
    f1.write(data)


f = open('mumbai.jpg','rb')

f1 = open('Mumbai.jpg','wb')

for i in f:
    f1.write(i)