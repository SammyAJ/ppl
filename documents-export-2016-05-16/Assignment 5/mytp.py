from Tkinter import *
class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        self.greet_button = Button(master, text="Hello", command=self.greet)
        self.greet_button.pack()
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()
    def greet(self):
        print("Hello")
root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
