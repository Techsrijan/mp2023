def even_check(n):
    if n%2==0:
        print("even")

'''
Think of lambdas as one-line methods without a name. They work practically the same as any other method in Python
https://stackabuse.com/map-filter-and-reduce-in-python-with-examples/
'''
even_check(22)

def eve_test(n):
    return n%2==0

def add(a,b):   #name add
    return a+b

f=lambda a,b:a+b  #without name
print(f(5,6))

g=lambda n:n%2==0
print(g(23))

