from numpy import *
arr=array([1,2,3,4,5])
print(arr,id(arr))

arr2=arr  #aliasing
print(arr2,id(arr2))

print("after change")
arr2[0]=1000
print(arr,id(arr))
print(arr2,id(arr2))

print("view")
# what if u want different address
arr3=array([1,2,3,4,5])
arr4=arr3.view()  #shallow copy
print(arr3,id(arr3))
print(arr4,id(arr4))

arr3[0]=46666
print(arr3,id(arr3))
print(arr4,id(arr4))

# what if u want change of one does not affect another and different address
print("copy")
arr5=array([1,2,3,4,5])
arr6=arr5.copy()   #deep copy
print(arr5,id(arr5))
print(arr6,id(arr6))

arr6[0]=442
print(arr5,id(arr5))
print(arr6,id(arr6))