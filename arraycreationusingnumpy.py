'''
there are 6 ways to create an array using numpy
1. array()
2. linspace()
3.  logspace()
4. arange()
5. zeros()
6. ones()


'''

from numpy import *

# array()
a=array([33,3,99,1])
print(a)
print(sort(a))

# linspace
arr=linspace(1,15,3)
print(arr)

#logspace
arr2=logspace(1,50)
print(arr2)

#arange()
arr3=arange(1,15,2)
print(arr3)

#zeros
arr4=zeros(10)
print(arr4)
print(arr4.dtype)

#ones

arr5=ones(40,int)
print(arr5+5)

print(arr5*33)

