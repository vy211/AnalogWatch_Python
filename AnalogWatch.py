# BY Vipin Yadav
import turtle
import time
def clock():
    
    h=turtle.Turtle()
    m=turtle.Turtle()
    s=turtle.Turtle()
    
    s.penup()
    h.penup()
    m.penup()
    s.speed(0)
    h.speed(0)
    m.speed(0)
    s.goto(0,100)
    m.goto(0,100)
    h.goto(0,100)
    m.left(90)
    s.left(90)
    h.left(90)
    m.pendown()
    h.pendown()
    s.pendown()
    while True:
    
        for i in range(59):
            s.forward(80)
            m.forward(70)
            h.forward(60)
            m.right(0.1)
            h.right(0.00833333333)
            
            time.sleep(1)
            s.right(6)
            s.goto(0,100)
            m.goto(0,100)
            h.goto(0,100)
            
            s.clear()
            m.clear()
            h.clear()
        
def design():
    vip = turtle.Turtle()
    vip.speed(0)
    vip.goto(0,-30)
    vip.begin_fill()
    vip.fillcolor("Blue")
    vip.circle(130)
    vip.end_fill()
    vip.goto(0,0)
    vip.begin_fill()
    vip.fillcolor("Pink")
    vip.circle(100)
    vip.end_fill()
    vip.penup()
    vip.goto(0,90)
    vip.left(60)
    for i in range(12):
        vip.forward(70)
        vip.write(i+1, move=False, align="center", font=("Arial",15 , "bold"))
        vip.goto(0,90)
        vip.right(30)
    
    

    


design()

clock()


