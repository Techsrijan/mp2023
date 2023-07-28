from turtle import *
t=Turtle()
sc=Screen()
def moveforward():
   t.forward(255)
   t.circle(50)

def movebackward():
   t.bk(100)

def moveleft():
   t.left(90)

def moveright():
   t.right(90)

sc.listen()
sc.onkey(moveforward,'Up')
sc.onkey(movebackward,'Down')
sc.onkey(moveleft,"Left")
sc.onkey(moveright,'Right')

done()
