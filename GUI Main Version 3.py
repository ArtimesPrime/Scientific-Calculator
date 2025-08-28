"""
GUI for main Calculator.
This version will include the GUI of the main calcultor as well as the function where the functional development will occur.
It will use for loops to create buttons and have a method of differentaiting which button is which, to allow them to preform their function.
18/07/25
"""

from tkinter import *
import math
import re

# The Class where all the calculator will be contained.
class calculator:

    #Initalising and defineing the properties of the program.
    def __init__(self):
        self.root = Tk()
        self.root.title("Calculator")
        self.container = Frame(self.root)
        self.container.grid(row=0, column=0, sticky=NSEW)

        self.TokenPattern = r"\d+(?:\.\d+)?|e|\u221A|π|(?:sin|cos|tan)(?:\u207B\u00B9)?|Log|Ln|[-+÷X/^()]"
        self.NumberPattern = r"-?\d+(?:\.\d+)?"
        self.FunctionPattern = r"((?:sin|cos|tan)(?:\u207B\u00B9)?|Log|Ln|u)"

        self.Operations = ["+","-","÷","X","^","\u221A", "Log", "Ln", "sin", "cos", "tan","sin\u207B\u00B9","cos\u207B\u00B9","tan\u207B\u00B9"]

        # Dictionary of the unique identifier of each button and its label.
        self.Labels = {
            (2, 0): "\u221A",
            (2, 1): "x\u00B2",
            (2, 2): "Log",
            (2, 3): "Menu",
            (2, 4): "F<->D",
            (3, 0): "\u00B2\u221A",
            (3, 1): "x\u02E3",
            (3, 2): "Ln",
            (3, 3): "(",
            (3, 4): ")",
            (4, 0): "sin",
            (4, 1): "cos",
            (4, 2): "tan",
            (4, 3): "π",
            (4, 4): "e",
            (5, 0): "sin\u207B\u00B9",
            (5, 1): "cos\u207B\u00B9",
            (5, 2): "tan\u207B\u00B9",
            (5, 3): "x/x",
            (5, 4): "AC",
            (6, 0): "1",
            (6, 1): "2",
            (6, 2): "3",
            (6, 3): "X",
            (6, 4): "÷",
            (7, 0): "4",
            (7, 1): "5",
            (7, 2): "6",
            (7, 3): "+",
            (7, 4): "-",
            (8, 0): "7",
            (8, 1): "8",
            (8, 2): "9",
            (8, 3): "DEL",
            (8, 4): "EXE",
            (9, 0): "0",
            (9, 1): "."}
       
        self.Answer = StringVar()
        self.Answer.set("")
        self.Quad = StringVar()
        self.Quad.set("")

        # Creates the dictionary of the frames and creates the frames
        self.frames = {}
        self.frames["Main Calculator"] = self.Main_Calculator()
        self.frames["Quadratic Solver"] = self.Quadratic_Solver()
        self.frames["Simultaneous Solver"] = self.Simultaneous_Solver()
        self.frames["Menu"] = self.Menu()

        # Configures the window
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        # Configures the container
        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(0, weight=1)

        # Displays the main calculator on start up.
        self.show_frame("Main Calculator")
   
    # Starts program
    def run(self):
        self.root.mainloop()
   
    # Displays the frames
    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()
   
    def Quadratic_Evaluation(self):
        print("yay")
   
    # Contains the operations preform by each button
    def Operators(self,r,c):
        match(r,c):
            case 2,0:
                self.Equationbox.insert("insert","( )\u221A")
            case 2,1:
                self.Equationbox.insert("insert","^2")
            case 2,2:
                self.Equationbox.insert("insert","Log")
            case 2,3:
                self.show_frame("Menu")
            case 2,4:
                pass
            case 3,0:
                self.Equationbox.insert("insert","(2)\u221A")
            case 3,1:
                self.Equationbox.insert("insert","^")
            case 3,2:
                self.Equationbox.insert("insert","Ln")
            case 3,3:
                self.Equationbox.insert("insert","(")
            case 3,4:
                self.Equationbox.insert("insert",")")
            case 4,0:
                self.Equationbox.insert("insert","sin")
            case 4,1:
                self.Equationbox.insert("insert","cos")
            case 4,2:
                self.Equationbox.insert("insert","tan")
            case 4,3:
                self.Equationbox.insert("insert","π")
            case 4,4:
                self.Equationbox.insert("insert","e")
            case 5,0:
                self.Equationbox.insert("insert","sin\u207B\u00B9")
            case 5,1:
                self.Equationbox.insert("insert","cos\u207B\u00B9")
            case 5,2:
                self.Equationbox.insert("insert","tan\u207B\u00B9")
            case 5,3:
                pass
            case 5,4:
                self.Equationbox.delete(0, END)
                self.Answer.set("")
            case 6,0:
                self.Equationbox.insert("insert","1")
            case 6,1:
                self.Equationbox.insert("insert","2")
            case 6,2:
                self.Equationbox.insert("insert","3")
            case 6,3:
                self.Equationbox.insert("insert","X")
            case 6,4:
                self.Equationbox.insert("insert","÷")
            case 7,0:
                self.Equationbox.insert("insert","4")
            case 7,1:
                self.Equationbox.insert("insert","5")
            case 7,2:
                self.Equationbox.insert("insert","6")
            case 7,3:
                self.Equationbox.insert("insert","+")
            case 7,4:
                self.Equationbox.insert("insert","-")
            case 8,0:
                self.Equationbox.insert("insert","7")
            case 8,1:
                self.Equationbox.insert("insert","8")
            case 8,2:
                self.Equationbox.insert("insert","9")
            case 8,3:
                pos = self.Equationbox.index(INSERT)
                self.Equationbox.delete(pos - 1)
               
            case 8,4:
                tokens = re.findall(self.TokenPattern, self.Equationbox.get())
                priority = {"+":1, "-":1, "÷":2, "X":2,
                            "^":3, "\u221A":3,
                            "Log":4, "Ln":4,
                            "sin":4, "cos":4, "tan":4,
                            "sin\u207B\u00B9":4, "cos\u207B\u00B9":4, "tan\u207B\u00B9":4,
                            "u":5
                            }
                postfix = []
                operators = []
                Last = None
                for i in tokens:
                    if re.match(self.NumberPattern, i) is not None:
                        postfix.append(i)
                    elif i == "-" and (Last == None or Last in {"^", "(", "+", "-", "X", "÷", "\u00B2\u221A", "\u221A"}):
                        operators.append("u")
                    elif i in self.Operations:
                        while operators and operators[-1] in priority and priority[operators[-1]] >= priority[i]:
                            postfix.append(operators.pop())
                            print(postfix)
                        operators.append(i)
                        print(postfix)
                    elif i == "e":
                        postfix.append(str(math.e))
                    elif i == "π":
                        postfix.append(str(math.pi))
                    elif i == "(":
                        operators.append(i)
                        print(postfix)
                    elif i == ")":
                        while operators and operators[-1] != "(":
                            postfix.append(operators.pop())
                            print(postfix)
                        operators.pop()
                    Last = i

                postfix += operators[::-1]
                print(postfix)
                output = []

                for i in postfix:

                    if re.match(self.NumberPattern, i) is not None:
                        output.append(i)
                    elif re.match(self.FunctionPattern, i) is not None:
                        try:
                            num3 = output.pop()
                        except IndexError:
                            self.Answer.set("Syntax Error")
                            return
                       
                        if i == "Log":
                            output.append(math.log10(float(num3)))
                        elif i == "Ln":
                            output.append(math.log(float(num3)))
                        elif i == "sin":
                            output.append(math.sin(float(num3)))
                        elif i == "cos":
                            output.append(math.cos(float(num3)))
                        elif i == "tan":
                            output.append(math.tan(float(num3)))
                        elif i == "sin\u207B\u00B9":
                            try:
                                output.append(math.asin(float(num3)))
                            except ValueError:
                                self.Answer.set("Domain Error")
                                return
                        elif i == "cos\u207B\u00B9":
                            try:
                                output.append(math.acos(float(num3)))
                            except ValueError:
                                self.Answer.set("Domain Error")
                                return
                        elif i == "tan\u207B\u00B9":
                            try:
                                output.append(math.atan(float(num3)))
                            except ValueError:
                                self.Answer.set("Domain Error")
                                return
                        elif i == "u":
                            output.append(-float(num3))

                    else:
                        print(output)
                        try:
                            num1 = float(output.pop())
                            num2 = float(output.pop())
                        except IndexError:
                            self.Answer.set("Syntax Error")
                            return
                        if i == "+":
                            output.append(num2+num1)
                        elif i == "-":
                            output.append(num2-num1)
                        elif i == "X":
                            output.append(num2*num1)
                        elif i == "÷":
                            output.append(num2/num1)
                        elif i == "\u221A":
                            if num1 < 0:
                                self.Answer.set("Math Error: Copmplex Domain Not Supported")
                                return
                            output.append(num1**(1/(num2)))
                        elif i == "^":
                            output.append(num2**num1)
                if len(output) > 1:
                    self.Answer.set("Syntax Error")
                    return
                Final = output[0]
                print(Final)
                if float(Final) > 0:
                    if float(Final) >= 10**16 or float(Final) <= 10**-16:
                        self.Answer.set("Math Error")
                        return
                else:
                    if float(Final) < -10**16:
                        self.Answer.set("Math Error")
                        return    
               
                self.Answer.set(Final)

            case 9,0:
                self.Equationbox.insert("insert","0")
            case 9,1:
                self.Equationbox.insert("insert",".")

   
    # The GUI of the main calculator
    def Main_Calculator(self):
        # Defining the frames properties
        frame = Frame(self.container)
        frame.rowconfigure([0,1,2,3,4,5,6,7,8,9], weight=1, minsize=30)
        frame.columnconfigure([0,1,2,3,4], weight=1, minsize=60)

        # Where the equation will be written
        self.Equationbox = Entry(frame, width=50,)  
        self.Equationbox.grid(row=0, columnspan=5, padx=5, pady=0, sticky = "NSEW")

        self.Answerbox = Label(frame, textvariable= self.Answer, bg="White", anchor="e")
        self.Answerbox.grid(row=1, columnspan=5, padx=5, pady=0,  sticky = "NSEW")

        # Creates the main mass of buttons
        for i in range(2, 6):
            for j in range(0,5):
                self.CenterButtons = Button(frame, text=self.Labels[(i,j)], width=5, command=lambda i=i, j=j: self.Operators(i, j))
                self.CenterButtons.grid(row=i, column=j, pady=6)
       
        # Creates the Side buttons
        for i in range(6,9):
            for j in range(3,5):
                self.RightButtons = Button(frame, text=self.Labels[(i,j)], width=5, command=lambda i=i, j=j: self.Operators(i, j))
                self.RightButtons.grid(row=i, column=j, pady=3)
       
        # Creates the Numberpad
        for i in range(6,9):
            for j in range(0,3):
                self.NumButtons = Button(frame, text=self.Labels[(i,j)], width=5, height=2, command=lambda i=i, j=j: self.Operators(i, j))
                self.NumButtons.grid(row=i, column=j, pady=3)

        # Creates the two buttons beneath the  numberpad.
        for i in range(9,10):
            for j in range(0,2):
                self.PlaceButtons = Button(frame, text=self.Labels[(i,j)], width=5, command=lambda i=i, j=j: self.Operators(i, j))
                self.PlaceButtons.grid(row=i, column=j, pady=3)

        frame.grid(row=0, column=0, sticky=NSEW)
        return frame
   
    def Menu(self):
        frame = Frame(self.container)
        frame.rowconfigure([0,1,2,3,4,5,6,7,8,9], weight=1, minsize=30)
        frame.columnconfigure([0], weight=1, minsize=300)

        self.MenuTitle = Label(frame, text="Menu", font="Verdana 20 bold")
        self.MenuTitle.grid(row=0, sticky=NSEW)


        self.MainButton = Button(frame, text="Main Calculator", height=3, command=lambda: self.show_frame("Main Calculator"))
        self.MainButton.grid(row=2, sticky=NSEW)


        self.QuadraticButton = Button(frame, text="Quadratic Solver", height=3, command=lambda: self.show_frame("Quadratic Solver"))
        self.QuadraticButton.grid(row=4, sticky=NSEW)


        self.SimultaneousButton = Button(frame, text="Simultaneous Solver", height=3, command=lambda: self.show_frame("Simultaneous Solver"))
        self.SimultaneousButton.grid(row=6, sticky=NSEW)
       
        frame.grid(row=0, column=0, sticky=NSEW)
        return frame

    def Quadratic_Solver(self):
        # Defining the frames properties
        frame = Frame(self.container)
        frame.rowconfigure([0,1,2,3,4,5,6,7,8,9], weight=1, minsize=30)
        frame.columnconfigure([0,1,2,3,4], weight=1, minsize=30)
        self.coefficents={}

        for i in range(1):
            for j in range(0,5,2):
                self.coefficents[f"QuadEntry{i}"] = Entry(frame, width=9)
                self.coefficents[f"QuadEntry{i}"].grid(row = 0, column=j, padx=3)

        self.QuadAnswerbox = Label(frame, textvariable= self.Quad, bg="White", anchor="w")
        self.QuadAnswerbox.grid(row=1, columnspan=5, padx=5, pady=0,  sticky = "NSEW")
           

        # Creates the main mass of buttons
        for i in range(2, 6):
            for j in range(0,5):
                self.CenterButtons = Button(frame, text=self.Labels[(i,j)], width=5, command=lambda i=i, j=j: self.Operators(i, j))
                self.CenterButtons.grid(row=i, column=j, pady=6)
       

        # Creates the Side buttons
        for i in range(6,9):
            for j in range(3,5):
                self.RightButtons = Button(frame, text=self.Labels[(i,j)], width=5, command=lambda i=i, j=j: self.Operators(i, j))
                self.RightButtons.grid(row=i, column=j, pady=3)


        self.NEWEXEButton = Button(frame, text="EXE", width = 5, command=lambda: self.Quadratic_Evaluation())
        self.NEWEXEButton.grid(row=8, column=4, pady=3)


        # Creates the Numberpad
        for i in range(6,9):
            for j in range(0,3):
                self.NumButtons = Button(frame, text=self.Labels[(i,j)], width=5, height=2, command=lambda i=i, j=j: self.Operators(i, j))
                self.NumButtons.grid(row=i, column=j, pady=3)
       

        # Creates the two buttons beneath the  numberpad.
        for i in range(9,10):
            for j in range(0,2):
                self.PlaceButtons = Button(frame, text=self.Labels[(i,j)], width=5, command=lambda i=i, j=j: self.Operators(i, j))
                self.PlaceButtons.grid(row=i, column=j, pady=3)

        frame.grid(row=0, column=0, sticky=NSEW)
        return frame


    def Simultaneous_Solver(self):
        pass
   

Calc = calculator()
Calc.run()

