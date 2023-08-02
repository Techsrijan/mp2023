class Student:
    def msg(self):  # self is the object of class
        print("This is class message")

    def __init__(self):
        print("this will run automatically when the object is created")

    def student_info(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)



s=Student()
s2=Student()
s.msg()
s2.msg()
s.student_info('abc',30)

'''
def student_info(name, age):
    name = name
    age = age
    print(name,age)

student_info('xyz',30)
'''
