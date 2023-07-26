import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(sys.getrecursionlimit()-500)
print(sys.getrecursionlimit())
def test():
    print("happy B-day")
    test()

test()