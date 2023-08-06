'''
class variable:
  1. instance variable -- each object hase its own value (self)
  2. class variable
'''
class Car:
    wheel=4    # class varable
    def __init__(self):
        self.mil=25      #instance variable
        self.name='Tata' #instance variable
    def msg(self):  # self is the object of class
        print("This is class message")


c1=Car()
c2=Car()

c1.msg()
print(c1.mil,c1.name,c1.wheel)
print(c2.mil,c2.name,c2.wheel)
c1.name='Maruti'
Car.wheel=8
print(c1.mil,c1.name,c1.wheel)
print(c2.mil,c2.name,c2.wheel)
