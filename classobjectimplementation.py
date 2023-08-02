class Student:
    def msg(self):  # self is the object of class
        print("This is class message")

s=Student()   # creation of object
Student.msg(s)# to explain the consecpt of self
# object.method() call
s.msg()    # use this

