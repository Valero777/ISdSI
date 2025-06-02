import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Flecha Móvil")

t = turtle.Turtle()
t.shape("triangle") 
t.color("white")
t.speed(10)
t.penup()  


speed = 20

def mover_arriba():
    t.setheading(90) 
    t.forward(speed)

def mover_abajo():
    t.setheading(270)  
    t.forward(speed)

def mover_izquierda():
    t.setheading(180)  
    t.forward(speed)

def mover_derecha():
    t.setheading(0)  
    t.forward(speed)

screen.listen() 
screen.onkey(mover_arriba, "Up")  
screen.onkey(mover_abajo, "Down")  
screen.onkey(mover_izquierda, "Left")  
screen.onkey(mover_derecha, "Right") 

turtle.done()