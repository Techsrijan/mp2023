from turtle import *
import time
wn=Screen()
t=Turtle()
wn.setup(420,320)
#screen.bgpic('bg.gif')
t.shape('turtle')
t.color('darkgoldenrod','black')
s=10
t.penup()
t.setpos(30,30)
for i in range(28):
        s=s+2
        t.stamp()
        t.forward(s)
        t.right(25)
        time.sleep(0.25)      #activated with a break of a 1/4th of a second
done()