'''print(range(10))
l=[]
l=range(1,10,2)
print(l)
'''
import time
for i in range(1,11):
    #print(i,'   ',end='')
    if i%2==0:
        #print("even=",i)
        pass
    else:
        print("odd=",i)


for i in range(1,11):
    if i%3==0:
        break
    else:
        print(i)

while True:
    print("Hello")