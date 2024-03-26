from turtle import Turtle,Screen
import random
import time

start=[100,200,300,-100,-200,-300]
screen = Screen()
screen.setup(width=1.0, height=1.0)
# screen.setup(width=400,height=300)




timmy = Turtle(shape="turtle")
timmy.color("medium blue")
timmy.name="timmy"


john=Turtle(shape="turtle")
john.color("orange red")
john.name="john"

kyle=Turtle(shape="turtle")
kyle.color("cyan")
kyle.name="kyle"

jason=Turtle(shape="turtle")
jason.color("magenta")
jason.name="jason"

mike=Turtle(shape="turtle")
mike.color("sea green")
mike.name="mike"

andy=Turtle(shape="turtle")
andy.color("olive")
andy.name="andy"



TurtleList=[andy,mike,jason,kyle,john,timmy]
bet=0
for turtles in TurtleList:

    turtles.penup()
    randomY = random.choice(start)
    start.remove(randomY)
    turtles.goto(x=-720, y=randomY)
    bet += int(screen.textinput(f"Bet for {turtles.name.title()}",f"his color is {turtles.pencolor()}") or "42")
    turtles.pendown()

GameStart=True

jenny=Turtle(shape="turtle")
jenny.color("indian red")
jenny.name="jenny"
jenny.penup()
jenny.speed(speed=4)
jenny.goto(720,400)
jenny.right(90)
jenny.pendown()
jenny.forward(730)
jenny.right(180)
jenny.forward(365)
jenny.left(90)
jenny.penup()
jenny.forward(150)
jenny.write("GO!!",font=('Arial', 20, 'normal'))

while GameStart:
    for turtles in TurtleList:
        if turtles.xcor()>=720:
            GameStart=False
            jenny.clear()
            jenny.write(f"{turtles.name} won the game\n.He get ${bet}",font=('Arial', 15, 'normal'))
        else:
            rand_distance = random.randint(0, 10)
            turtles.forward(rand_distance)


screen.mainloop()



