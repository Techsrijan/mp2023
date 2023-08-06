class Theory:
    def t_marks(self):
        print("this is theory marks")

    def __init__(self):
        print("this is class Theory constructor")



class Sessional:
    def s_marks(self):
        print("this is Sessional marks")

    def __init__(self):
        print("this is class sESSIONAL constructor")

class Result(Sessional,Theory):
    def r_marks(self):
        print("this is result")


s=Result()
s.t_marks()
s.s_marks()
s.r_marks()