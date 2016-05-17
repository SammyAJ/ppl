from turtle import *
import turtle 
from math import *
class ellipse() :
    def __init__(self) :
        print "\n \t This is a Ellipse"
    def __area1__(self) :
        self.r1 = input("Enter the radius1")
	self.r2 = input("Enter the radius2")
	self.A = self.r1 * self.r2 * 3.142
	print "Area of Ellipse : "
	print self.A
    def __circumference1__(self) :
        self.P = 2 * 3.142 * sqrt(((self.r1 * self.r1) + (self.r2 * self.r2)) / 2)
	print "Perimeter of circle"
	print self.P
    def __draw1__(self) :
	shapesize(self.r1,self.r2)
	fillcolor("lightgreen")
	pencolor("black")	
	exitonclick()

if __name__ == "__main__":
	e = ellipse()
	e.__area1__()
	e.__circumference1__()
	e.__draw1__()


