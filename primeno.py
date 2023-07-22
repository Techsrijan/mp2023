n=int(input("enter any number"))
i=2
while i<=n-1:
    if n%i==0:
        print("not prime")
        break

    i=i+1
else:    # loop else will run when loop not runs properly
    print(" prime")