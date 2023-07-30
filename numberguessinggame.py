import random as r
# n=r.randint(4,50)
# print(n)
#
# for i in range(4):
#     a = int(input("enter any number between 4 to 50"))
#     print(a)
#     if n==a:
#         print("you are win")
#         break
#
# else:
#     print("har gaye")


num=r.randint(4,50)
print(num)
chance=5
while chance>0:
    user = int(input("enter any number between 4 to 50"))
    print(num)
    if num == user:
        print("you are win")
        break
    chance=chance-1
else:
    print("har gaye")
