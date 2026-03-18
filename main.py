from turtle import *

t = Turtle()

#Plano Cartesiano
t.pu()
t.goto(-300, 0)
t.pd()
t.fd(600)
t.stamp()
t.pu()
t.goto(0, -300)
t.pd()
t.lt(90)
t.fd(600)
t.stamp()

#Formas
t.pu()
t.goto(75, 150)
t.pd()
t.rt(45)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(135)
t.fd(143)

t.pu()
t.goto(-75, 150)
t.pd()
t.fd(175)
t.rt(90)
t.fd(90)
t.rt(90)
t.fd(175)
t.rt(90)
t.fd(90)

t.pu()
t.goto(-75, -150)
t.pd()
for _ in range(8):
    t.fd(75)
    t.rt(45)











mainloop()