def fact(n):
    if n==0:
        return 1
    return n*(fact(n-1))




a=int(input("enter any number"))
print(fact(a))

print(__name__)
