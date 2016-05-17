from turtle import *
import turtle 
from math import *
class Circle() :
    def __init__(self) :
        print "\n \t This is a Circle"
    def __area__(self) :
        self.r = input("Enter the radius")
	self.A = self.r * self.r * 3.142
	print "Area of Circle : "
	print self.A
    def __circumference__(self) :
        self.P = 2 * 3.142 * self.r
	print "Circumference of circle"
	print self.P
    def __draw__(self) :
        penup()
	goto(0, -100)
	shape("circle")
	shapesize(self.r,self.r)
	fillcolor("lightgreen")
	pencolor("black")	
	exitonclick()

if __name__ == "__main__":
	c = Circle()
	c.__area__()
	c.__circumference__()
	c.__draw__()

