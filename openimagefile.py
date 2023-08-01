f=open("test.gif","rb")
p=open("best.gif","ab")
for data in f:
    print(data)
    p.write(data)