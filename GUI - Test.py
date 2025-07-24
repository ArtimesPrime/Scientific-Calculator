"""
Calculator Main Version 1
This version will inculde the "Body" of the calculator the gui, as well as being able to execute the Basic operations + - / *
18/07/25
"""


from tkinter import *
import math


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




        self.show_frame("Main Calculator")
   
    def run(self):
        self.root.mainloop()
   
    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()
    
    def Operators(self,r,c):
        match(r,c):
            case 1,0:
                pass
   
    def Main_Calculator(self):
        frame = Frame(self.container)
        frame.rowconfigure([0,1,2,3,4,5,6,7,8], weight=1, minsize=30)
        frame.columnconfigure([0,1,2,3,], weight=1, minsize=60)

        self.Equationbox = Text(frame, width=40, height=2)
        self.Equationbox.grid(row=0, columnspan=8,pady=5, padx=5)


        for i in range(1, 6):
            for j in range(4):
                self.CenterButtons = Button(frame, text="center", width=5, command=lambda i=i, j=j: self.Operators(i, j))
                self.CenterButtons.grid(row=i, column=j, pady=3)
        


        for i in range(6,9):
            for j in range(2,4):
                self.RightButtons = Button(frame, text="Right", width=5, command=lambda i=i, j=j: self.Operators(i, j))
                self.RightButtons.grid(row=i, column=j, pady=3)

        frame.grid(row=0, column=0)
        return frame

    def Numbers(self):
        Frame(self.container)


    def Quadratic_Solver(self):
        pass


    def Simultaneous_Solver(self):
        pass




Calc = calculator()
Calc.run()


