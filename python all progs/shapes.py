class Shapes() :	
	pass
	class circle (Shapes) :
		def __Area__(self) :
			r = input("Enter the radius");
			A = r * r * 3.142
			print "Area of circle : "
			print A
			return A
		
		def __Perimeter__(self) :
			P = 2 * 3.142 * r
			print "Perimeter of circle"
			print P
			return P

		def __DrawC__(self) :
			from turtle import *
			penup()
			goto(0, -100)
			shape("circle")
			shapesize(2,6,1)
			fillcolor("red")
			pencolor("darkred")	
			exitonclick()
