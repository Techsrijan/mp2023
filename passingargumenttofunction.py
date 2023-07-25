'''
pass an agument to function
1. positional argument
2. keyword argument
3. default argument
4. variable length argument (*)
5. keyword variable length argumnent
'''

#1. positional argument
def person(name,age):
    print("Name=",name)
    age=age+10
    print("age=",age)


person('pradeep',66)

#person(66,'person')

#2. keyword argument
person(name='rohan',age=88)
person(age=55,name='mohan')


#4. variable length argument (*)

def add(a,b,d):
    c=a+b+d
    print("Sum=",c)

add(33,66,55)

def addvar(a,*b):
   print(a)
   print(*b,(type(b)))
   sum=a
   for i in b:
       sum=sum+i
   return sum

print(addvar(1,2,5,4,3,3))

def addvar3(*b):
   print(*b,(type(b)))
   sum=0
   for i in b:
       sum=sum+i
   return sum
print(addvar3(555,5,8,9,26,6,8,9))