import turtle

# Our gameplay screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('blue')

# Create player turtle
player = turtle.Turtle()
player.shape('turtle')
player.color('green')
player.penup()
player.goto(-250, 0)

# Create finish line
finish = turtle.Turtle()
finish.penup()
finish.goto(250, -150)
finish.pendown()
finish.forward(0)
finish.left(90)
finish.forward(300)
finish.hideturtle()

# Create an obstacle
obstacle = turtle.Turtle()
obstacle.shape('square')
obstacle.color('red')
obstacle.penup()
obstacle.goto(0, 50)

screen.listen()

# Movement for player
while True:
    key = screen.textinput("Move", "Enter"
                                   "w/a/s/d to move")
    
    if key == "w":
        player.sety(player.ycor() + 20)
    elif key == "s":
        player.sety(player.ycor() - 20)
    elif key == "a":
        player.setx(player.xcor() - 20)
    elif key == "d":
        player.setx(player.xcor() + 20)
        
    if player.xcor() > 250:
        print('Congratulations! You won !')
        break


              






