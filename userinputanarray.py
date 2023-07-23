from array import *

arr=array('i',[])

n=int(input("How many students u have"))
for i in range(n):
    num=int(input("enter the marks of student"))
    arr.append(num)

print(arr)

search=int(input("enter the marks u want to find"))

for k in range(len(arr)):
    if arr[k]==search:
        print("Item found=", search)
        break
else:
    print("Item not found")


# search with index method
print(arr.index(search))