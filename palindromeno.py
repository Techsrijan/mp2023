n=int(input("enter any number"))
print("main n=",n)
orig=n
rev=0
while n>0:
    a=n%10
    rev=rev*10+a
    n=n//10
print(rev)
print("n=",n)
if rev==orig:
    print("Plaindrome no")
else:
    print("not palindrome")