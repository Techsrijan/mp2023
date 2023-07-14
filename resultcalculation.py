h=int(input("Enter the marks of hindi"))
e=int(input("Enter the marks of english"))
m=int(input("Enter the marks of math"))
c=int(input("Enter the marks of c language"))
p=int(input("Enter the marks of python language"))

total=h+e+m+c+p
print("Total marks=",total)

per=total/5

print("Percentage=",per)

if per<33:
    print("Fail")
elif per>=33 and per<45:
    print("Third")
elif per>=45 and per<60:
    print("Second")
elif per>=60:
    print("First")
