import time
n=int(input("enter the no of toffee"))
i=1
stock=15
while i<=n:
    if i<=stock:
        print("Please collect toffe=",i)
        time.sleep(1)
    else:
        print("out of stock")
        break
    i=i+1
else:
    print("thank you please visit again")
