x=500
def test():
    x=5
    global y
    y=500
    a=globals()['x']
    print("Global local=",a)  #500
    print("local=",x)

test()
print(x)
print(y)

def best():
    print("local=",y)
best()

