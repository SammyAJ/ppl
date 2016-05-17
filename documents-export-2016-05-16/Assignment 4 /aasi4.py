from turtle import *
import turtle 
from math import *
class Shape () :
	def __init__(self) :
		print "\n \t This is the shape class "
class Ellipse(Shape) :
	def __init__(self) :
		print "\n \t This is the Ellipse class "
class Circle(Ellipse) :
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
class ellipse(Shape) :
    def __init__(self) :
        print "\n \t This is a Ellipse"
    def __area__(self) :
        self.r1 = input("Enter the radius1")
	self.r2 = input("Enter the radius2")
	self.A = self.r1 * self.r2 * 3.142
	print "Area of Ellipse : "
	print self.A
    def __circumference__(self) :
        self.P = 2 * 3.142 * sqrt(((self.r1 * self.r1) + (self.r2 * self.r2)) / 2)
	print "Perimeter of circle"
	print self.P
    def __draw__(self) :
        penup()
	goto(0, -100)
	shape("circle")
	shapesize(self.r1,self.r2)
	fillcolor("lightgreen")
	pencolor("black")	
	exitonclick()
class Polygon(Shape) :
	def __init__(self) :
		print "\n \t This is the Polygon class "
class Line () :
	def __init__(self) :
		print "This is the line"
		self.l = input("Enter the length")
	def __draw__(self) :
    		self.l = self.l * 10
		turtle.forward(self.l)
		exitonclick()
class Square() :
    def __init__(self) :
        print "\n \t This is a Sqaure"
    def __area__(self) :
        self.r = input("Enter the side")
	self.A = self.r * self.r 
	print "Area of Square: "
	print self.A
    def __perimeter__(self) :
        self.P = 2 * self.r
	print "Perimeter of Square :"
	print self.P
    def __draw__(self) :
        penup()
	goto(0, -100)
	shape("square")
	shapesize(self.r)
	fillcolor("lightgreen")
	pencolor("black")	
	exitonclick()
class rectangle() :
    def __init__(self) :
        print "\n \t This is a Rectangle"
    def __area__(self) :
        self.r1 = input("Enter the length")
	self.r2 = input("Enter the breadth")
	self.A = self.r1 * self.r2
	print "Area of Rectangle: "
	print self.A
    def __perimeter__(self) :
        self.P = self.r1 + self.r2
	print "Perimeter of rectangle"
	print self.P
    def __draw__(self) :
        penup()
	goto(0, -100)
	shape("square")
	shapesize(self.r1,self.r2)
	fillcolor("lightgreen")
	pencolor("black")	
	exitonclick()
class rtriangle() :
    def __init__(self) :
        print "\n \t This is a Rightangled triangle"
    def __area__(self) :
        self.h = input("Enter the height")
	self.b = input("Enter the base")
	self.A = (self.b * self.h) / 2
	print "Area of Right angle Triangle : "
	print self.A
    def __perimeter__(self) :
        self.P = self.h + self.b + sqrt((self.h * self.h) + (self.b * self.b))
	print "Perimeter of Right angled Triangle"
	print self.P
    def __draw__(self) :
    	self.b = self.b * 10
    	self.h = self.h * 10
    	self.hy = ((self.b * self.b) + (self.h * self.h))
	turtle.goto(self.b,0)
    	turtle.goto(0,self.h)
    	turtle.goto(0,0)
	exitonclick()

class itriangle() :
    def __init__(self) :
        print "\n \t This is a Isosceles Triangle"
    def __area__(self) :
        self.h = input("Enter the height")
	self.b = input("Enter the base")
	self.A = (self.b * self.h) / 2
	print "Area of Isosceles Triangle: "
	print self.A
    def __perimeter__(self) :
	self.s = input("Enter the side of triangle")
        self.P = 2 * self.s + self.b
	print "Perimeter of Isosceles Triangle"
	print self.P
    def __draw__(self) :
        penup()
	goto(0, -100)
	shape("triangle")
	shapesize(self.s,self.b,self.h)
	fillcolor("lightgreen")
	pencolor("black")	
	exitonclick()

class eqitriangle() :
    def __init__(self) :
        print "\n \t This is a Eqilateral tritangle"
    def __area__(self) :
	self.s = input("Enter the side")
	self.A = ((sqrt(3) / 4 ) * (self.s * self.s))
	print "Area of Eqilateral tritangle: "
	print self.A
    def __perimeter__(self) :
        self.P = 3 * self.s
	print "Perimeter of Eqilateral tritangle"
	print self.P
    def __draw__(self) :
        penup()
	goto(0, -100)
	shape("triangle")
	shapesize(self.s)
	fillcolor("lightgreen")
	pencolor("black")	
	exitonclick()

class pentagon() :
    def __init__(self) :
        print "\n \t This is a Pentagon"
    def __area__(self) :
	self.s = input("Enter the side")
	self.A = (sqrt(5 * (5 + 2 * sqrt(5))) * (self.s * self.s)) / 4 
	print "Area of Pentagon"
	print self.A
    def __perimeter__(self) :
        self.P = 5 * self.s
	print "Perimeter of Pentagon"
	print self.P
    def __draw__(self) :
	for j in(1,2,3):
		turtle.fillcolor("lightgreen")
		turtle.pencolor("black")
    		turtle.forward(self.s * 10)
    		turtle.left(72)
    		turtle.forward(self.s * 10)
    		turtle.left(72)
	exitonclick()
	
class hexagon() :
    def __init__(self) :
        print "\n \t This is a Hexaagon"
    def __area__(self) :
	self.s = input("Enter the side")
	self.A = (3 * sqrt(3)) * (self.s * self.s) / 4 
	print "Area of Hexagon"
	print self.A
    def __perimeter__(self) :
        self.P = 6 * self.s
	print "Perimeter of Hexagon"
	print self.P
    def __draw__(self) :
	for j in(1,2,3):
    		turtle.forward(self.s * 10)
    		turtle.left(60)
    		turtle.forward(self.s * 10)
    		turtle.left(60)
		fillcolor("lightgreen")
		pencolor("black")	
	exitonclick()
	
class heptagon() :
    def __init__(self) :
        print "\n \t This is a Heptagon"
    def __area__(self) :
	self.s = input("Enter the side")
	self.A = (7 * (self.s * self.s) * cos(180 / 7) )/ 4 
	print "Area of Heptagon"
	print self.A
    def __perimeter__(self) :
        self.P = 7 * self.s
	print "Perimeter of Heptagon"
	print self.P
    def __draw__(self) :
	for j in(1,2,3,4):
    		turtle.forward(self.s * 10)
    		turtle.left(51.428571429)
    		turtle.forward(self.s * 10)
    		turtle.left(51.428571429)
		fillcolor("lightgreen")
		pencolor("black")	
	exitonclick()
	
class octagon() :
    def __init__(self) :
        print "\n \t This is a Octagon"
    def __area__(self) :
	self.s = input("Enter the side")
	self.A = ((2 * (1 + sqrt(2))) * (self.s * self.s))
	print "Area of Octagon"
	print self.A
    def __perimeter__(self) :
        self.P = 8 * self.s
	print "Perimeter of Octagon"
	print self.P
    def __draw__(self) :
	for j in(1,2,3,4):
    		turtle.forward(self.s * 10)
    		turtle.left(45)
    		turtle.forward(self.s * 10)
    		turtle.left(45)
		fillcolor("lightgreen")
		pencolor("black")	
	exitonclick()
	
class nonagon() :
    def __init__(self) :
        print "\n \t This is a Nonagon"
    def __area__(self) :
	self.s = input("Enter the side")
	self.A = ((9 * (self.s * self.s) / 4 ) * cos(180 / 9) ) / 4
	print "Area of Nonagon"
	print self.A
    def __perimeter__(self) :
        self.P = 9 * self.s
	print "Perimeter of Nonagon"
	print self.P
    def __draw__(self) :
	for j in(1,2,3,4,5):
    		turtle.forward(self.s * 10)
    		turtle.left(40)
    		turtle.forward(self.s * 10)
    		turtle.left(40)
		fillcolor("lightgreen")
		pencolor("black")	
	exitonclick()
	
if __name__ == "__main__":
	S = Shape()
	print "1) Ellipse"
	print "2) Polygon"
	c = input("enter which shape do want to learn ? ")
	if(c==1) :
		B = Ellipse()
		print "1) Circle"
		print "2) ellipse"
		a = input("enter the shape you want to see ")
		if(a==1) :
			c = Circle() 
			c.__area__()
			c.__circumference__()
			c.__draw__()	
		elif(a==2) : 
			c = ellipse() 
			c.__area__()
			c.__circumference__()
			c.__draw__()
	elif(c==2) : 
		C = Polygon()
		print "1) Line"
		print "2) Square"
		print "3) Rectangle"
		print "4) Rightangled Triangle"
		print "5) Isosceles Triangle"
		print "6) Eqilateral Triangle"
		print "7) Pentagon"
		print "8) Hexagon"
		print "9) Heptagon"
		print "10) Octagon"
		print "11) Nonagon"
		s = input("enter your choice")
		if(s==1) :
			c = Line() 
			c.__draw__()	
		elif(s==2) : 
			c = Square() 
			c.__area__()
			c.__perimeter__()
			c.__draw__()
		elif(s==3) : 
			c = rectangle() 
			c.__area__()
			c.__perimeter__()
			c.__draw__()
		elif(s==4) : 
			c = rtriangle()
			c.__area__()
			c.__perimeter__()
			c.__draw__()
		elif(s==5) : 
			c = itriangle()
			c.__area__()
			c.__perimeter__()
			c.__draw__()
		elif(s==6) : 
			c = eqitriangle()
			c.__area__()
			c.__perimeter__()
			c.__draw__()
		elif(s==7) : 
			c =pentagon ()
			c.__area__()
			c.__perimeter__()
			c.__draw__()
		elif(s==8) : 
			c = hexagon ()
			c.__area__()
			c.__perimeter__()
			c.__draw__()
		elif(s==9) : 
			c =heptagon ()
			c.__area__()
			c.__perimeter__()
			c.__draw__()
		elif(s==10) : 
			c =octagon ()
			c.__area__()
			c.__perimeter__()
			c.__draw__()
		elif(s==11) : 
			c =nonagon ()
			c.__area__()
			c.__perimeter__()
			c.__draw__()
	else :
		print "You entered wrong choice"
			
