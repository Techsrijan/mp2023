#import array
from array import *
#array creation and initilization
a=array('f',[1,2,3,4,5.0])
print(a)

for i in a:
    print(i)

k=0
print(len(a))

while k<len(a):
    print(a[k])
    k=k+1

for l in range(0,len(a)):
    print(a[l])

print(a.buffer_info())

print(a.typecode)