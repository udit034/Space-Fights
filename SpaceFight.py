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
		
class Player( Sprite ):
	def __init__( self, spriteshape, color, startx, starty, speed, lives ):
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
		
player = Player( "triangle", "white", 0, 0, 1, 3 )
turtle.onkey( player.turn_left, "Left" )
turtle.onkey( player.turn_right, "Right" )
turtle.onkey( player.accelerate, "Up" )
turtle.onkey( player.decelerate, "Down" )
turtle.listen()

while True:
	player.move()
	


delay = input( "Enter" )