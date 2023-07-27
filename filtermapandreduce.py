from functools import reduce
l=[1,5,68,7,88,92,55,33,2,4]

g=lambda n:n%2==0

even=list(filter(g,l))
print(even)

s=lambda a:a+10

data=list(map(s,even))
print(data)


add=lambda a,b:a+b

output=reduce(add,data)
print(output)


