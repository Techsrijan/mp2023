
f=open("bello.txt","r")

#print(f.read())  # whole content
print(" redline output")
#print(f.readlines(3))
#print(f.readline(11))  # no of character in a file

for data in f:
    print(data)

f.close()  # to close the file

f=open("bello.txt","w")
f.write("how are u")
f.close()


f=open("bello.txt","a")
f.write("Kaise ho")