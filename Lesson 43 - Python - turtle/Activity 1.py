import turtle 
screen = turtle.Screen()
screen.bgcolor("dark blue")
screen.title("Turtle Graphics")

board = turtle.Turtle()
board.speed("fastest")
board.hideturtle()


colors = ["red", "orange", "yellow", "lime", "cyan", "violet", "pink", "white"]
for i in range(90):
    board.color(colors[i % len(colors)])
    board.width(4)
    board.forward(i * 2)
    board.right(91)
turtle.done()