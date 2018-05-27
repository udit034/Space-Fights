import os
import random
import turtle

turtle.bgcolor("black")
'''
turtle.fd(0)
turtle.speed(0)
turtle.ht()
turtle.setundobuffer(1)
turtle.tracer(1)
'''

class Sprite( turtle.Turtle ):
	def __init__( self, spriteshape, color, startx, starty, speed ):
		turtle.Turtle.__init__( self, shape=spriteshape )
		self.penup()
		self.color( color )
		self.fd( 0 )
		self.goto( startx, starty ) 
		self.speed = speed
		
	def move( self ):
		self.fd( self.speed )
		
		if self.xcor() > 290 or self.ycor() > 290 or self.xcor() < -290 or self.ycor() < -290:
			self.rt(60)
		
class Player( Sprite ):
	def __init__( self, spriteshape, color, startx=0, starty=0, speed=1, lives=3 ):
		Sprite.__init__( self, spriteshape, color, startx, starty, speed )
		self.lives = lives
		
	def accelerate( self ):
		self.speed += 1
		
	def decelerate( self ):
		self.speed -= 1
		
	def turn_left( self ):
		self.lt( 45 )
		
	def turn_right( self ):
		self.rt( 45 )
		
class Game():
	def __init__(self, level=1, score=0, state="playing", lives=3 ):
		self.level = level
		self.score = score
		self.state = state
		self.lives = lives
		self.pen = turtle.Turtle()
	
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
		
		
game = Game()		
game.draw_border()
		
player = Player( "triangle", "white", 0, 0, 1, 3 )
turtle.onkey( player.turn_left, "Left" )
turtle.onkey( player.turn_right, "Right" )
turtle.onkey( player.accelerate, "Up" )
turtle.onkey( player.decelerate, "Down" )
turtle.listen()

while True:
	player.move()
	


delay = input( "Enter" )