## TYPES OF ARGUMENTS

def person(name , age):
    print(name)
    print(age)

person(age=28,name='navin')

def person(name , age=18):
    print(name)
    print(age)

person('navin',28)

# Variable Length Arguments:-
def sum(*b):
   c = 0
   for i in b:
       c = c + i

   print(c)

sum(5,6,34,78)

## KWARGS
def person(name, **data):
    print(name)
    print(data)
person('navin',age=28,city='Mumbai',mob=9865432)


def person(name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)
person('navin',age=28,city='Mumbai',mob=9865432)