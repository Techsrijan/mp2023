from numpy import *
arr=array([
    [1,2,3,4],
    [2,3,4,5],
    [2,3,4,5],
])


arr2=array([
    [1,2,3,4],
    [2,3,4,5],
    [2,3,4,5],
])

arr3=arr+arr2
print(arr3)

a=array([
    [1,2,3],
    [4,5,6]
])


b=array([
    [2,2,4],
    [3,2,4],
    [6,7,8]
])

mul=a@b
print(mul)

print(dot(a,b))