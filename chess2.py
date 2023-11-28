import turtle
p=turtle.Turtle()
p.pensize(5)
p.pencolor("pink")
p.speed(9)

def square():
    for i in range(4):
        p.forward(40)
        p.right(90)
    p.forward(40)

for i in range(8):
    p.penup()
    p.goto(0,40*i) 
    p.pendown()

    for x in range(8):
        if (x+i)%2 ==0:
            color="black"
        else:
            color="white"

        p.fillcolor(color)
        p.begin_fill()
        square()
        p.end_fill()
        
