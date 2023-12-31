# import required modules
import turtle
import time
import random
import math

delay = 0.1
score = 0
high_score = 0
headSize = 1
ghostspeed = 3
ghost2speed = 3
ghost3speed = 3
ghost4speed = 3


MAX_SCORE = 200


# Creating a window screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("Black")
# the width and height can be put as user's choice
wn.setup(width=800, height=800)
wn.tracer(0)

# user's turtle
head = turtle.Turtle()
head.shape("circle")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"
head.shapesize(headSize, headSize, headSize)  

# food in the game
food = turtle.Turtle()
food.shape("circle")
food.color("green")
food.direction = "stop"
food.penup()
x = random.randint(-270, 270)
y = random.randint(-270, 270)
food.goto(x, y)

#ghost in the game
ghost = turtle.Turtle()
ghost.shape("triangle")
ghost.color("red")
ghost.direction = "stop"
ghost.penup()
x = random.randint(-270, 270)
y = random.randint(-270, 270)
ghost.goto(x, y)

#ghost #2 in the game
ghost2 = turtle.Turtle()
ghost2.shape("triangle")
ghost2.color("yellow")
ghost2.direction = "stop"
ghost2.penup()
ghost2.hideturtle()


#ghost #3 in the game
ghost3 = turtle.Turtle()
ghost3.shape("triangle")
ghost3.color("blue")
ghost3.direction = "stop"
ghost3.penup()
ghost3.hideturtle()



#ghost #4 in the game
ghost4 = turtle.Turtle()
ghost4.shape("triangle")
ghost4.color("pink")
ghost4.direction = "stop"
ghost4.penup()
ghost4.hideturtle()



pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0 High Score : 0", align="center",
		font=("candara", 24, "bold"))


#Out of bounds border
border = turtle.Turtle()
border.color("white")
border.penup()
border.goto(-300, 300)
border.pendown()
border.goto(300, 300)
border.goto(300, -300)
border.goto(-300, -300)
border.goto(-300, 300)
border.hideturtle()




# assigning key directions
def goup():
	head.direction = "up"


def godown():
    head.direction = "down"


def goleft():
	head.direction = "left"


def goright():
    head.direction = "right"



def boundDetection(obj):
	#Top Left Corner
	if obj.xcor() <= -280 & obj.ycor() >= 280:
		obj.direction = random.choice(["right", "down"])
		boundFlag = 1

	#Top Right Corner
	elif obj.xcor() >= 280 & obj.ycor() >= 280:
		obj.direction = random.choice(["left", "down"])
		boundFlag = 1

	#Bottom Left Corner
	elif obj.xcor() <= -280 & obj.ycor() <= -280:
		obj.direction = random.choice(["right", "up"])
		boundFlag = 1

	#Bottom Right Corner
	elif obj.xcor() >= 280 & obj.ycor() <= -280:
		obj.direction = random.choice(["left", "up"])
		boundFlag = 1


	#Top Wall
	elif obj.ycor() >= 280:
		obj.direction = random.choice(["right", "left", "down"])
		boundFlag = 1


	#Bottom Wall
	elif obj.ycor() <= -280:
		obj.direction = random.choice(["right", "left", "up"])
		boundFlag = 1


	#Left Wall 
	elif obj.xcor() <= -280:
		obj.direction = random.choice(["right", "down", "up"])
		boundFlag = 1

	
	#Right Wall 
	elif obj.xcor() >= 280:
		obj.direction = random.choice(["down", "left", "up"])
		boundFlag = 1

	else: 
		boundFlag = 0


def avoid():
	if math.fabs(head.xcor() - food.xcor()) < math.fabs(head.ycor() - food.ycor()):
		if head.xcor() < food.xcor():
			food.direction = "right"

		elif head.xcor() > food.xcor():
			food.direction = "left"

	elif math.fabs(head.xcor() - food.xcor()) > math.fabs(head.ycor() - food.ycor()):
		if head.ycor() < food.ycor():
			food.direction = "up"

		elif head.ycor() > food.ycor():
			food.direction = "down"


def chase(obj): 
	if math.fabs(head.xcor() - obj.xcor()) > math.fabs(head.ycor() - obj.ycor()):
		if head.xcor() < obj.xcor():
			obj.direction = "left"

		elif head.xcor() > obj.xcor():
			obj.direction = "right"

	elif math.fabs(head.xcor() - obj.xcor()) < math.fabs(head.ycor() - obj.ycor()):
		if head.ycor() < obj.ycor():
			obj.direction = "down"

		elif head.ycor() > obj.ycor():
			obj.direction = "up"


def move():
	if head.direction == "up":
		y = head.ycor()
		head.sety(y+10)
	if head.direction == "down":
		y = head.ycor()
		head.sety(y-10)
	if head.direction == "left":
		x = head.xcor()
		head.setx(x-10)
	if head.direction == "right":
		x = head.xcor()
		head.setx(x+10)


def movefood(count):
	if count == 5 & boundFlag != 1: 
		avoid()

	if boundFlag == 0:
		boundDetection(food)

	if food.direction == "up":
		y = food.ycor()
		food.sety(y+10)
	if food.direction == "down":
		y = food.ycor()
		food.sety(y-10)
	if food.direction == "left":
		x = food.xcor()
		food.setx(x-10)
	if food.direction == "right":
		x = food.xcor()
		food.setx(x+10)


def moveghost(count, obj, objspeed):
	if count == 5 & boundFlag != 1:
		if obj == ghost:
			chase(obj)
		else :
			randommovement(obj)
		
	if boundFlag == 0:
		boundDetection(obj)

	if obj.direction == "up":
		y = obj.ycor()
		obj.sety(y+objspeed)
	if obj.direction == "down":
		y = obj.ycor()
		obj.sety(y-objspeed)
	if obj.direction == "left":
		x = obj.xcor()
		obj.setx(x-objspeed)
	if obj.direction == "right":
		x = obj.xcor()
		obj.setx(x+objspeed)

def randommovement(obj): 
	obj.direction = random.choice(["left", "right", "up", "down"])

	


wn.listen()
wn.onkeypress(goup, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")

directionFlag = 0
boundFlag = 0

ghost2.goto(300,300)
ghost3.goto(300,300)
ghost4.goto(300,300)


# Main Gameplay
while True:
	wn.update()
	movefood(directionFlag)
	moveghost(directionFlag, ghost, ghostspeed)
	if ghost2.isvisible(): moveghost(directionFlag, ghost2, ghost2speed)
	if ghost3.isvisible(): moveghost(directionFlag, ghost3, ghost3speed)
	if ghost4.isvisible(): moveghost(directionFlag, ghost4, ghost4speed)

	if directionFlag == 5:
		directionFlag = 0
	else:
		directionFlag += 1

	if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290 or head.distance(ghost) < (headSize + (headSize*3)) + 10 or  head.distance(ghost2) < (headSize + (headSize*3)) + 10 or head.distance(ghost3) < (headSize + (headSize*3)) + 10 or  head.distance(ghost4) < (headSize + (headSize*3)) + 10:
		time.sleep(1)
		head.goto(0, 0)
		head.direction = "Stop"
		headSize = 1
		head.shapesize(headSize, headSize, headSize)
		colors = random.choice(['red', 'blue', 'green'])
		shapes = random.choice(['square', 'circle'])
		score = 0
		delay = 0.1 
		pen.clear()
		pen.write("Score : {} High Score : {} ".format(
			score, high_score), align="center", font=("candara", 24, "bold"))
		x = random.randint(-270, 270)
		y = random.randint(-270, 270)
		ghost.goto(x, y)
		ghost2.hideturtle()
		ghost3.hideturtle()
		ghost4.hideturtle()


		
	if head.distance(food) < (headSize + (headSize*3)) + 20:
		x = random.randint(-270, 270)
		y = random.randint(-270, 270)
		food.goto(x, y)
		delay -= 0.001
		score += 10
		headSize += 0.5
		ghostspeed += 1

		if score == 50: 
			x = random.randint(-270, 270)
			y = random.randint(-270, 270)
			ghost2.goto(x, y)
			ghost2.showturtle()

		if score == 100: 
			x = random.randint(-270, 270)
			y = random.randint(-270, 270)
			food.goto(x, y)
			ghost3.showturtle()

		if score == 150: 
			x = random.randint(-270, 270)
			y = random.randint(-270, 270)
			ghost4.goto(x,y)
			ghost4.showturtle()

		if ghost2.isvisible() : ghost2speed += 1
		if ghost3.isvisible() : ghost2speed += 1
		if ghost4.isvisible() : ghost2speed += 1

		head.shapesize(headSize, headSize, headSize)
		if score > high_score:
			high_score = score
		
		if score >= MAX_SCORE:
			time.sleep(1)
			head.goto(0, 0)
			head.direction = "Stop"
			headSize = 1
			head.shapesize(headSize, headSize, headSize)
			colors = random.choice(['red', 'blue', 'green'])
			shapes = random.choice(['square', 'circle'])
			score = 0
			delay = 0.1 
			pen.clear()
			pen.write("Score : {} High Score : {} ".format(
			score, high_score), align="center", font=("candara", 24, "bold"))
		
		pen.clear()
		pen.write("Score : {} High Score : {} ".format(
			score, high_score), align="center", font=("candara", 24, "bold"))
		


	move()
	time.sleep(delay)

wn.mainloop()
