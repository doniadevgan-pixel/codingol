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

# there are two color options for the turtle graphics: "dark blue" and "black". You can change the background color by modifying the line `screen.bgcolor("dark blue")` to `screen.bgcolor("black")`.