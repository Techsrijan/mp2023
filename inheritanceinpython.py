'''
deriving a new class from the base class is known
as inheritance.


'''
class Room:         # parent class or base class
    def area(self,l,b):
        self.l=l
        self.b=b
        s=self.l*self.b
        print("area=",s)

class GuestRoom(Room):  # child class or derived class
    def msg(self):
        print("this is guest room")


# r=Room()
# r.area(50,10)

g=GuestRoom()
g.msg()
g.area(40,50)