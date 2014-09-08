import turtle

def draw_stuff():
    window = turtle.Screen()
    window.bgcolor('red')

    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('yellow')
    brad.speed('2')

    for i in range(0,4):
        brad.forward(100)
        brad.right(90)

    dianna = turtle.Turtle()
    dianna.speed(8)
    dianna.color('green')

    for i in range(0,3):
        dianna.forward(100)
        dianna.right(120)
        
    window.exitonclick()
        
draw_stuff()