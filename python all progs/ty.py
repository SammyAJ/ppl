from turtle import *
from math import *
class Circle() :
    def __init__(self) :
        print "This is a Circle"
    def __area__(self) :
        self.r = input("Enter the radius")
	self.A = self.r * self.r * 3.142
	print "Area of circle : "
	print self.A
	return self.A
    def __circumference__(self) :
        self.P = 2 * 3.142 * self.r
	print "Circumference of circle"
	print self.P
	return self.P
    def __draw__(self) :
        penup()
	goto(0, -100)
	shape("circle")
	shapesize(self.r,self.r,2)
	fillcolor("lightgreen")
	pencolor("black")	
	exitonclick()
class Ellipse() :
    def __init__(self) :
        print "This is a Ellipse"
    def __area__(self) :
        self.r1 = input("Enter the radius1")
	self.r2 = input("Enter the radius2")
	self.A = self.r1 * self.r2 * 3.142
	print "Area of Ellipse : "
	print self.A
	return self.A
    def __circumference__(self) :
        self.P = 2 * 3.142 * sqrt(((self.r1 * self.r1) + (self.r2 * self.r2)) / 2)
	print "Circumference of circle"
	print self.P
	return self.P
    def __draw__(self) :
        penup()
	goto(0, -100)
	shape("circle")
	shapesize(self.r1,self.r2,2)
	fillcolor("lightgreen")
	pencolor("black")	
	exitonclick()
class Square() :
    def __init__(self) :
        print "This is a Sqaure"
    def __area__(self) :
        self.r = input("Enter the side")
	self.A = self.r * self.r 
	print "Area of Square: "
	print self.A
	return self.A
    def __perimeter__(self) :
        self.P = 2 * self.r
	print "Perimeter of Square :"
	print self.P
	return self.P
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
        print "This is a rectangle"
    def __area__(self) :
        self.r1 = input("Enter the length")
	self.r2 = input("Enter the breadth")
	self.A = self.r1 * self.r2
	print "Area of Rectangle: "
	print self.A
	return self.A
    def __perimeter__(self) :
        self.P = self.r1 + self.r2
	print "Perimeter of rectangle"
	print self.P
	return self.P
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
        print "This is a right angle triangle"
    def __area__(self) :
        self.h = input("Enter the height")
	self.b = input("Enter the base")
	self.A = (self.b * self.h) / 2
	print "Area of Right angle Triangle : "
	print self.A
	return self.A
    def __perimeter__(self) :
        self.P = self.h + self.b + sqrt((self.h * self.h) + (self.b * self.b))
	print "Perimeter of circle"
	print self.P
	return self.P
    def __draw__(self) :
        penup()
	goto(0, -100)
	shape("triangle")
	shapesize(self.b,self.h)
	fillcolor("lightgreen")
	pencolor("black")	
	exitonclick()

class itriangle() :
    def __init__(self) :
        print "This is a Isosclas Triangle"
    def __area__(self) :
        self.h = input("Enter the height")
	self.b = input("Enter the base")
	self.A = (self.b * self.h) / 2
	print "Area of Isosclas Triangle: "
	print self.A
	return self.A
    def __perimeter__(self) :
	self.s = input("Enter the side of triangle")
        self.P = 2 * self.s + self.b
	print "Perimeter of Isosclas Triangle"
	print self.P
	return self.P
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
        print "This is a Eqilateral tritangle"
    def __area__(self) :
	self.s = input("Enter the side")
	self.A = ((sqrt(3) / 4 ) * (self.s * self.s))
	print "Area of Eqilateral tritangle: "
	print self.A
	return self.A
    def __perimeter__(self) :
        self.P = 3 * self.s
	print "Perimeter of Eqilateral tritangle"
	print self.P
	return self.P
    def __draw__(self) :
        penup()
	goto(0, -100)
	shape("triangle")
	shapesize(self.s)
	fillcolor("lightgreen")
	pencolor("black")	
	exitonclick()


print "1) Circle"
print "2) Square"
print "3) Ellipse"
print "4) Rectangle"
print "5) Rightangled Triangle"
print "6) Isosclas Triangle"
print "7) Eqilateral Triangle"

s = input("enter your choice")
if(s==1) :
	c = Circle() 
	c.__area__()
	c.__circumference__()
	c.__draw__()	
elif(s==2) : 
	c = Square() 
	c.__area__()
	c.__perimeter__()
	c.__draw__()
elif(s==3) : 
	c = Ellipse() 
	c.__area__()
	c.__circumference__()
	c.__draw__()
elif(s==4) : 
	c = rectangle() 
	c.__area__()
	c.__perimeter__()
	c.__draw__()
elif(s==5) : 
	c = rtriangle()
	c.__area__()
	c.__perimeter__()
	c.__draw__()
elif(s==6) : 
	c = itriangle()
	c.__area__()
	c.__perimeter__()
	c.__draw__()
elif(s==7) : 
	c = eqitriangle()
	c.__area__()
	c.__perimeter__()
	c.__draw__()
else :
	print "Enter wrong choice"



