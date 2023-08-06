'''
types of methods in class
1. instance method ---which accepts self as argument
2. class method -- which accepts cls as argument
3. static method - which accepts no argument
'''

class Test:
    school='Techsrijan'
    def marks(self,m1,m2,m3,m4): #instance method
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.m4=m4
        return (self.m1+self.m2+self.m3+self.m4)

    @classmethod  # decorator
    def school_name(cls):
        return cls.school

    @staticmethod
    def best():   # it will runwithout any object
        print("this will run without any argument")

Test.best()
s=Test()
print(s.marks(10,20,3,40))
print(Test.school_name())
s.best()
