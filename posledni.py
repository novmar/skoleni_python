import turtle


# turtle.shape("turtle")
# turtle.color("black","blue")

# turtle.forward(100)
# turtle.done()

class Turtle:
    def __init__(self,step):
        self.step = step
        turtle.shape("turtle")
        turtle.color("black","green")

    def go(self):
        turtle.forward(self.step)

    def left(self):
        turtle.left(90)
    def right(self):
        turtle.right(90)


t=Turtle(25)
t.go()
commands= {
    "go" : t.go,
    "left": t.left,
    "right": t.right
}
# with open("path.txt") as stream:
#     for line in stream:
#         print(line.strip())
#         # method=commands[line.strip()]
#         # method()
#         commands[line.strip()]()
#
screen = turtle.Screen()
screen.onkey(t.go,"Up")
screen.onkey(t.left,"Left")
screen.onkey(t.right,"Right")
screen.listen()
turtle.mainloop()



turtle.done()
