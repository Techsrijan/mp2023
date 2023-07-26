# keyword variable length argument
def person(**data):
    print(data)
    for i,j in data.items():
        print(i,j)

person(name='ashwani',age=25,pin=273001,city='gkp')


#default argument
def facebookaccount(name,age=18):
    print(name,age)

facebookaccount(name='abc')
facebookaccount(name='xyz',age=25)
