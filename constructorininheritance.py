class A:
    def __init__(self):
        print("this is class A constructor")


class B(A):
    def __init__(self):
        super().__init__()
        print("this is class B constructor")


class C(B):
    def __init__(self):
        super().__init__()
        print("this is class C constructor")


s=C()