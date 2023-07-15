from math import *
a=int(input("Enter First number"))
b=int(input("Enter Second number"))
c=int(input("Enter Three number"))

d=b*b-4*a*c
print(d)

if d==0:
    x1=x2=-b/(2*a)
    print("Roots are real and equal")
    print("X1=",x1,"x2=",x2)
elif d>0:
    x1=(-b+sqrt(d))/(2*a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print("Roots are real and unequal")
    print("X1=", x1, "x2=", x2)
elif d<0:
    print("roots are imginary")