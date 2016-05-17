class ComplexNum() :
    def __init__(self) :
        self.a = complex(input("Enter the 1st complex number : "))
        self.b = complex(input("Enter the 2nd complex number : "))
    def __add__(self) :
        self.c = self.a + self.b
        print self.c
    def __sub__(self) :
                self.c = self.a - self.b
                print self.c
    def __mul__(self) :
                self.c = self.a * self.b
                print self.c
    def __div__(self) :
                self.c = self.a / self.b
                print self.c

c = ComplexNum() 

c.__add__()
c.__sub__()
c.__mul__()
c.__div__()


