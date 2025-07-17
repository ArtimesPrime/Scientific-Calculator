""" 
Calculator Main Version 1
This version will inculde the "Body" of the calculator the gui, as well as being able to execute the Basic operations + - / *
18/07/25
"""

from tkinter import *

class calculator:
    def __init__(self):
        self.root = Tk()
        self.root.title("Calculator")
        self.container = Frame(self.root)
        self.container.grid(row=0, column=0, sticky=NSEW)

        self.frames = {}


        self.frames["Main Calculator"] = self.Main_Calculator()
        self.frames["Quadratic Solver"] = self.Quadratic_Solver()
        self.frames["Simultaneous Solver"] = self.Simultaneous_Solver()

        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(0, weight=1)


        self.show_frame("Main calculator")
    
    def run(self):
        self.root.mainloop()
    
    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()
    
    def Main_Calculator(self):
        frame = Frame(self.container)
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)


    def Quadratic_Solver(self):
        pass

    def Simultaneous_Solver(self):
        pass


Calc = calculator()
Calc.run()


