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
#Forma 1
color = textinput("Obter cor","Digite a cor desejada:")

t.pu()
t.goto(75, 150)
t.pd()
t.color("red")
t.begin_fill()
t.fillcolor(color)
t.rt(45)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(135)
t.fd(143)
t.end_fill()

#Forma 2
color = textinput("Obter cor","Digite a cor desejada:")

t.pu()
t.goto(-75, 150)
t.pd()
t.color("orange")
t.begin_fill()
t.fillcolor(color)
t.fd(150) 
t.lt(60)
t.fd(100)
t.lt(120)
t.fd(150)
t.lt(60)
t.fd(100)
t.end_fill()

#Forma 3
color = textinput("Obter cor","Digite a cor desejada:")

t.pu()
t.goto(-75, -150)
t.pd()
t.color("blue")
t.begin_fill()
t.fillcolor(color)
t.rt(105)
for _ in range(8):
    t.fd(75)
    t.rt(45)
t.end_fill()

#Forma 4
color = textinput("Obter cor","Digite a cor desejada:")

t.pu()
t.goto(75, -150)
t.pd()
t.color("green")
t.begin_fill()
t.fillcolor(color)
t.lt(45)
t.fd(200)
t.lt(120)
t.fd(100)
t.lt(60)
t.fd(100)
t.lt(60)
t.fd(100)
t.lt(120)
t.end_fill()

#Espiral
t.pu()
t.goto(200, 130) 
t.pd()
for i in range(100):
    t.fd(i)
    t.rt(45)


mainloop()