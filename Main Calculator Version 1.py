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
   
    def Main_Calculator(self):
        frame = Frame(self.container)
        frame.rowconfigure([0,1,2,3,4,5,6,7,8], weight=1, minsize=30)
        frame.columnconfigure([0,1,2,3,], weight=1, minsize=60)


        self.Equationbox = Entry(frame, justify=LEFT)
        self.Equationbox.grid(row=0, columnspan=8)

        self.Multiplication_Button = Button(frame, text="×", font="Verdana 12 bold", width=5)
        self.Multiplication_Button.grid(row=6, column=2)

        self.Division_Button = Button(frame, text="÷", font="Verdana 12 bold", width=5 )
        self.Division_Button.grid(row=6, column=3)

        self.Addition_Button = Button(frame, text="+",font="Verdana 12 bold", width=5)
        self.Addition_Button.grid(row=7, column=2)


        self.Subtraction_Button = Button(frame, text="-", font="Verdana 12 bold", width=5)
        self.Subtraction_Button.grid(row=7, column=3)

        self.Del_Button = Button(frame, text="Del", font="Verdana 12 bold", width=5)
        self.Del_Button.grid(row=8, column=2)

        self.EXE_Button = Button(frame, text="EXE", font="Verdana 12 bold", width=5)
        self.EXE_Button.grid(row=8, column=3)

        self.Euler_Button = Button(frame, text="e", font="Verdana 12 bold", width=5)
        self.Euler_Button.grid(row=5, column=2)

        self.AC_Button = Button(frame, text="AC", font="Verdana 12 bold", width=5)
        self.AC_Button.grid(row=5, column=3)

        self.Pi_Button = Button(frame, text="π", font="Verdana 12 bold", width=5)
        self.Pi_Button.grid(row=5, column=1)

        self.Menu_Button = Button(frame, text="Menu", font="Verdana 12 bold", width=5)
        self.Menu_Button.grid(row=5, column=0)

        self.Fraction_Button = Button(frame, text="x/x", font="Verdana 12 bold", width=5)
        self.Fraction_Button.grid(row=4, column=0)

        self.F_To_D_Button = Button(frame, text="F<->D", font="Verdana 12 bold", width=5)
        self.F_To_D_Button.grid(row=4, column=1)

        self.LBracket_Button = Button(frame, text="(", font="Verdana 12 bold", width=5)
        self.LBracket_Button.grid(row=4, column=2)

        self.RBracket_Button = Button(frame, text=")", font="Verdana 12 bold", width=5)
        self.RBracket_Button.grid(row=4, column=3)

        self.sin_Inverse_Button = Button (frame, text="sin\u207B\u00B9", font="verdana 12 bold", width=5)
        self.sin_Inverse_Button.grid(row=3, column=0)

        self.cos_Inverse_Button = Button (frame, text="cos\u207B\u00B9", font="verdana 12 bold", width=5)
        self.cos_Inverse_Button.grid(row=3, column=1)        

        self.tan_Inverse_Button = Button (frame, text="tan\u207B\u00B9", font="verdana 12 bold", width=5)
        self.tan_Inverse_Button.grid(row=3, column=2)  

        self.Natural_Log_Button = Button(frame, text="ln", font="verdana 12 bold", width=5)
        self.Natural_Log_Button.grid(row=3,column=3)

        self.sin_Button = Button(frame, text="sin", font="Verdana 12 bold", width=5)
        self.sin_Button.grid(row=2,column=0)

        self.cos_Button = Button(frame, text="cos", font="Verdana 12 bold", width=5)
        self.cos_Button.grid(row=2,column=1)

        self.tan_Button = Button(frame, text="tan", font="Verdana 12 bold", width=5)
        self.tan_Button.grid(row=2,column=2)

        self.Log_Button = Button(frame, text="log", font="Verdana 12 bold", width=5)
        self.Log_Button.grid(row=2, column=3)

        self.Square_Root_Button = Button(frame, text="U+221A", font="Verdana 12 bold", width=5)
        self.Square_Root_Button.grid(row=1, column=0)


        frame.grid(row=0, column=0)
        return frame


    def Quadratic_Solver(self):
        pass


    def Simultaneous_Solver(self):
        pass




Calc = calculator()
Calc.run()


