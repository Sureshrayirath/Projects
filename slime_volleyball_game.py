#The code creates a simple Slime Volleyball game using Turtle. A ball falls with gravity,
#  bounces off the ground and player, and reflects on collision. The player moves left or 
# right with arrow keys, and updates occur continuously using timers.



import turtle
import math
import time

# Setup screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Slime Volleyball")
wn.tracer(0)

# Player setup
player = turtle.Turtle()
player.shape("circle")
player.color("yellow")
player.shapesize(3.0, 3.0)
player.penup()
player.goto(0, -200)
player.dx = 0

# Ball setup
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.shapesize(1.0, 1.0)
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = 5

# Constants
GRAVITY = -0.2
GROUND = -250

# Player controls
def move_left():
    player.dx = -5

def move_right():
    player.dx = 5

def stop():
    player.dx = 0

wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeyrelease(stop, "Left")
wn.onkeyrelease(stop, "Right")

# Update loop
def update():
    # Move player
    player.setx(player.xcor() + player.dx)

    # Keep player inside bounds
    if player.xcor() < -300:
        player.setx(-300)
    elif player.xcor() > 300:
        player.setx(300)

    # Ball gravity
    ball.dy += GRAVITY
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Ground collision
    if ball.ycor() < GROUND + 10:
        ball.sety(GROUND + 10)
        ball.dy *= -0.7  # bounce
        if abs(ball.dy) < 0.5:
            ball.dy = 0

    # Wall collision
    if ball.xcor() > 350 or ball.xcor() < -350:
        ball.dx *= -1

    # Collision with player
    if ball.distance(player) < 50 and ball.ycor() < player.ycor() + 60:
        # Compute reflection
        angle = math.atan2(ball.ycor() - player.ycor(), ball.xcor() - player.xcor())
        speed = math.sqrt(ball.dx**2 + ball.dy**2)
        ball.dx = math.cos(angle) * speed
        ball.dy = math.sin(angle) * speed + 5  # small boost on hit

    wn.update()
    wn.ontimer(update, 20)  # run again in 20ms

# Start game loop
update()
wn.mainloop()
