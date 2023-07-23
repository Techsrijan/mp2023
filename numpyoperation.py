from numpy import *

arr=array([1,2,3,4])
arr2=array([3,4,5,4])

a=arr+arr2
print(a)

print(arr.min())
print(arr.max())
print(sum(arr))

print(arr.shape)

print(arr.ndim)

print(concatenate([arr,arr2]))