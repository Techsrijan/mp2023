from math import *
# function definition
def greet():
    print("Good morning")

greet()    #function call

print("Kya hal hi")
greet()

def test():
    pass

# here a and b are called formal arguments
def add(a,b):
    c=a+b
    print("Sum=",c)

add(40,50)

x=int(input("enter any number"))
y=int(input("enter any number"))
add(x,y)
# here x and y are called actual arguments


print(sqrt(36))

# function returning a value
def add2(p,q):
    c=p+q
    f=p-q
    return c,f

print(add2(5,6))

d,e=add2(55,66)
print("Zod=",d," e=",e)

x=print("hello")
print("X=",x)