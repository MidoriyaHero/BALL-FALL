import turtle
import random
import pygame 
import glob
pygame.mixer.init()
class Ball(turtle.Turtle):
    gravity = -0.05  # pixels/(time of iteration)^2
    energy_loss_ground = 0.95
    energy_loss_walls = 0.8

    def __init__(self, x=0, y=0):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.y_velocity = random.randint(-10, 50) / 10
        self.x_velocity = random.randint(-30, 30) / 10
        self.setposition(x, y)
        self.size = int(random.gammavariate(25, 0.8))
        self.color((random.random(),
                    random.random(),
                    random.random())
                   )
    def draw(self):
        self.clear()
        self.dot(self.size)

    def move(self):
        self.y_velocity += self.gravity
        self.sety(self.ycor() + self.y_velocity)
        self.setx(self.xcor() + self.x_velocity)

    def bounce_floor(self, floor_y):
        if self.ycor() < floor_y:
            self.y_velocity = -self.y_velocity * self.energy_loss_ground
            self.sety(floor_y)
            sound_list = glob.glob("C:/Users/buitr/CODE/Self_Study_PJ/BALL-FALL/Music/*.wav")
            sound_file = random.choice(sound_list)
            pygame.mixer.Sound(sound_file).play()  # Add this line for the sound

    def bounce_walls(self, wall_x):
        if abs(self.xcor()) > wall_x:
            self.x_velocity = -self.x_velocity * self.energy_loss_walls
            sign = self.xcor() / abs(self.xcor())
            self.setx(wall_x * sign)
            sound_list = glob.glob("C:/Users/buitr/CODE/Self_Study_PJ/BALL-FALL/Music/*.wav")
            sound_file = random.choice(sound_list)
            pygame.mixer.Sound(sound_file).play()


# Simulation code
width = 300
height = 200

window = turtle.Screen()
window.setup(width, height)
window.tracer(0)

balls = [Ball() for _ in range(1)]
count = 1
def add_ball(x, y):
    balls.append(Ball(x, y))

window.onclick(add_ball)

while True:
    for ball in balls:
        ball.draw()
        ball.move()
        ball.bounce_floor(-height/2)
        ball.bounce_walls(width/2)
    if balls[-1].ycor() == height :
        count = count*2
    for i in range(count):
        balls.append(Ball(0, 0))
    window.update()