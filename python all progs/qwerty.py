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
class Shape(Circle, ellipse) :
	def __init__(self):
        	Circle.__init__(self)
        	ellipse.__init__(self)
if __name__ == "__main__":
	x = Shape()
	x.__area__()
	x.__circumference__()	
	x.__draw__()
	x.__area1__()
	x.__circumference1__()
	x.__draw1__()
	
		
