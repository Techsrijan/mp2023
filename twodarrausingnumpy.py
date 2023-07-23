from numpy import *
arr=array([
    [1,2,3,4],
    [2,3,4,5],
    [2,3,4,5],
])

print(arr)
print(arr.shape)
print(arr.ndim)

arr2=arr.flatten() #to create one dimension array
print(arr2)

arr3=arr2.reshape(4,3)
print(arr3)

print("3-d")
arr4=arr2.reshape(2,2,3)
print(arr4)
print(arr4.ndim)
