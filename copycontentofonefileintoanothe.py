f=open("cello.txt","r")
p=open("copyfile.txt","a")
for data in f:
    print(data)
    p.write(data)