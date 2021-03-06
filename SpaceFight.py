import os
import random
import turtle
import winsound

turtle.fd(0)
turtle.speed(0)
turtle.bgcolor("black")
turtle.ht()
turtle.setundobuffer(1)
turtle.tracer(1)

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Fights")
wn.bgpic("b1.gif")

turtle.register_shape("s1.gif")
turtle.register_shape("s2.gif")
turtle.register_shape("s3.gif")
turtle.register_shape("l1.gif")

class Sprite( turtle.Turtle ):
	def __init__( self, spriteshape, color, startx, starty, speed ):
		turtle.Turtle.__init__( self, shape=spriteshape )
		self.speed(0)
		self.penup()
		self.color( color )
		self.fd( 0 )
		self.goto( startx, starty ) 
		self.speed = speed
		
	def move( self ):
		self.fd( self.speed )
		
		if self.xcor() > 290 or self.ycor() > 290 or self.xcor() < -290 or self.ycor() < -290:
			self.rt(60)
			
	def is_collision( self, other ):
		if ( self.xcor() >= (other.xcor() - 20) ) and \
		( self.xcor() <= (other.xcor() + 20) ) and \
		( self.ycor() >= (other.ycor() - 20) ) and \
		( self.ycor() <= (other.xcor() + 20) ):
			return True
		else:
			return False	
		
class Player( Sprite ):
	def __init__( self, spriteshape, color, startx=0, starty=0, speed=4, lives=3 ):
		Sprite.__init__( self, spriteshape, color, startx, starty, speed )
		self.lives = lives
		self.shapesize( 50,50, 50 )
		
	def accelerate( self ):
		self.speed += 1
		
	def decelerate( self ):
		self.speed -= 1
		
	def turn_left( self ):
		self.lt( 45 )
		
	def turn_right( self ):
		self.rt( 45 )

class Missile( Sprite ):
	def __init__( self, spriteshape, color, startx, starty, speed=20 ):
		Sprite.__init__( self, spriteshape, color, startx, starty, speed=20 )
		self.shapesize( stretch_wid=2, stretch_len=2, outline=None)
		self.speed = speed
		self.status = "ready"
		self.goto( -1000, 1000 )
		
	def fire( self ):
		if self.status == "ready":
			#winsound.PlaySound('laser.wav', winsound.SND_FILENAME)
			self.goto( player.xcor(), player.ycor() )
			self.setheading( player.heading() )
			self.status = "firing"
	
	def move( self ):
		if self.status == "ready":
			self.goto( -1000, 1000 )
			
		if self.status == "firing":
			self.fd( self.speed )
			
		if  self.xcor() > 290 or self.ycor() > 290 or self.xcor() < -290 or self.ycor() < -290:
			self.goto( -1000, 1000 )
			self.status="ready"
		

			
class Enemy( Sprite ):
	def __init__( self, spriteshape="circle", color="red", startx=-100, starty=0, speed=6):
		Sprite.__init__( self, spriteshape, color, startx, starty, speed )
		self.setheading( random.randint( 0, 360 ) )
		
class Ally( Sprite ):
	def __init__( self, spriteshape="circle", color="red", startx=-100, starty=0, speed=8):
		Sprite.__init__( self, spriteshape, color, startx, starty, speed )
		self.setheading( random.randint( 0, 360 ) )
	
	def move( self ):
		self.fd( self.speed )
		if self.xcor() > 290 or self.ycor() > 290 or self.xcor() < -290 or self.ycor() < -290:
			self.lt(60)	
	
		
class Game():
	def __init__(self, level=1, score=0, state="playing", lives=3 ):
		self.level = level
		self.score = score
		self.state = state
		self.lives = lives
		self.pen = turtle.Turtle()
		self.lives = 3
	
	def draw_border( self ):
		self.pen.speed( 0 ) 
		self.pen.color( "white" )
		self.pen.pensize( 3 )
		self.pen.penup()
		self.pen.goto( -300, 300 )
		self.pen.pendown()
		for side in range(4):
			self.pen.fd( 600 )
			self.pen.rt( 90 )
		self.pen.penup()
		self.pen.ht()
		self.pen.pendown()
		
	def update_status( self ):
		self.pen.undo()
		msg = "Score: %s"%(self.score)
		self.pen.penup()
		self.pen.goto( -300, 310 )
		self.pen.write( msg, font=( "Arial", 16, "normal" ) ) 
		
game = Game()		
game.draw_border()
		
player = Player( "s3.gif", "white", 0, 0, 1, 4 )
missile = Missile( "l1.gif", "yellow", 0, 0 )

enemies = []
for i in range( 4 ):
	enemies.append( Enemy( "s1.gif", "red", -100, 0, 6 ) )

	
allies = []
for i in range( 4 ):
	allies.append( Ally( "s2.gif", "blue", 0, 0 ) )


turtle.onkey( player.turn_left, "Left" )
turtle.onkey( player.turn_right, "Right" )
turtle.onkey( player.accelerate, "Up" )
turtle.onkey( player.decelerate, "Down" )
turtle.onkey( missile.fire, "space" )
turtle.listen()

while True:
	player.move()
	missile.move()
	
	for enemy in enemies:
		enemy.move()
		if player.is_collision( enemy ):
			x = random.randint( -250, 250 )
			y = random.randint( -250, 250 )
			enemy.goto( x, y )
		
		if missile.is_collision( enemy ):
			winsound.PlaySound('explosion.wav', winsound.SND_FILENAME)
			x = random.randint( -250, 250 )
			y = random.randint( -250, 250 )
			enemy.goto( x, y )
			missile.status = "ready"
			game.score += 100
			game.update_status()
	
	for ally in allies:
		ally.move()
		if missile.is_collision( ally ):
			winsound.PlaySound('explosion.wav', winsound.SND_FILENAME)
			x = random.randint( -250, 250 )
			y = random.randint( -250, 250 )
			ally.goto( x, y )
			missile.status = "ready"
			game.score -= 100
			game.update_status()
		
	
