import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor('red')

    joe = turtle.Turtle()
    joe.shape('turtle')
    joe.color('green')
    joe.speed(1) # on a scale of 1 to 10, where 10 is fastest

    for i in range(0,4):
        joe.forward(100)
        joe.right(90)

    window.exitonclick()

draw_square()