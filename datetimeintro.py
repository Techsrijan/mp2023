from datetime import *

'''
https://www.w3schools.com/python/python_datetime.asp
'''

x=datetime.now()
print(x)
print(x.year)
print(x.strftime("%a"))
print(x.strftime("%I"))
print(x.strftime("%M"))
print(x.strftime("%S"))