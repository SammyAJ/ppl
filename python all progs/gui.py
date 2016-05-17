import Tkinter
import tkMessageBox
from Tkinter import *
class Gui () :
	def __init__(self) :
		print "Hello"
	def __gu__(self) :
		self.top = Tkinter.Tk()
		def __helloCallBack__(self):
   			selftkMessageBox.showinfo( "Hello Python", "Hello World")
			self.B = Tkinter.Button(top, text ="Hello", command = helloCallBack)
			self.B.pack()
			self.top.mainloop()

if __name__ == "__main__":
	a = Gui()
	a.__gu__()

