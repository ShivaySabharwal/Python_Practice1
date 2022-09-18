class Student:

    school = 'PuP'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    #Instance Method:-
    def averagem(self):
        return (self.m1+self.m2+self.m3)/3
    #Accessors:-
    def getm1(self):
        return self.m1
    #Mutators:-
    def setm1(self, value):
        self.m1 = value

    #Class Methods:-
    @classmethod
    def getSchool(cls):
        print(cls.school)

    #Static Method
    @staticmethod
    def info():
        print("This is Student Class...")


s1 = Student(44,55,66)
s2 = Student(77,88,99)

print(s1.m1)
print(Student.school)

avg = s1.averagem()
print(avg)

Student.getSchool()

Student.info()