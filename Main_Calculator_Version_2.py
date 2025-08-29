"""
Main Calculator Version 2
Built ontop of Version 1 of GUI which explains similar Comments
and Version 1 of Main Calculator
V1 Featues: Basic operators and Constants
V2 Features: Log ,Exponents and Preliminary Error Prevention
By Ethan Beale"""

from tkinter import * #Creates GUI
import math # Preforms more advanced Math operations
import re # Allows for regex patterns and search mathods

# The Class where all the calculator will be contained.
class calculator:

    #Initalising and defineing the properties of the program.
    def __init__(self):
        self.root = Tk()
        self.root.title("Calculator")
        self.container = Frame(self.root)
        self.container.grid(row=0, column=0, sticky=NSEW)

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

        # Creates the dictionary of the frames and creates the frames
        self.frames = {}
        self.frames["Main Calculator"] = self.Main_Calculator()
        self.frames["Quadratic Solver"] = self.Quadratic_Solver()
        self.frames["Simultaneous Solver"] = self.Simultaneous_Solver()

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
    
    # Contains the operations preform by each button
    def Operators(self,r,c):
        match(r,c):
            case 2,0:
                # Every Line in this formatt does the same thing. Append to equationbox.
                self.Equationbox.insert("insert","( )\u221A")
            case 2,1:
                self.Equationbox.insert("insert","^2")
            case 2,2:
                self.Equationbox.insert("insert","Log")
            case 2,3:
                pass
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
                pass
            case 4,1:
                pass
            case 4,2:
                pass
            case 4,3:
                self.Equationbox.insert("insert","π")
            case 4,4:
                self.Equationbox.insert("insert","e")
            case 5,0:
                pass
            case 5,1:
                pass
            case 5,2:
                pass
            case 5,3:
                pass
            case 5,4:
                # Clears Equation and Answer box
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
                # Deletes based on where the text pointer is.
                pos = self.Equationbox.index(INSERT)
                self.Equationbox.delete(pos - 1)
                
            case 8,4:
                # Creates a list from the equation that breaks at relevant segements.
                tokens = re.findall(r"\d+(?:\.\d+)?|e|\u221A|π|sin|cos|tan|Log|Ln|[-+÷X/^()]", self.Equationbox.get())
                # Facilitates Order of operations
                priority = {"+":1, "-":1, "÷":2, "X":2, "^":3, "\u221A":3, "Log":4, "Ln":4}
                # Postfix is output of the next block
                postfix = []

                # Stack that allows operators to be handled correctly.
                operators = []

                # Turns Infix into Postifx
                for i in tokens:
                    if re.match(r"\d+(?:\.\d+)?", i) is not None:
                        postfix.append(i)
                    elif i in ["+","-","÷","X","^","\u221A", "Log", "Ln"]:
                        # This makes sure the operators are in the correct order.
                        while operators and operators[-1] in priority and priority[operators[-1]] >= priority[i]:
                            postfix.append(operators.pop())
                        operators.append(i)
                    # Detecting and adding constants
                    elif i == "e":
                        postfix.append(str(math.e))
                    elif i == "π":
                        postfix.append(str(math.pi))

                    # Handles bracket indentation
                    elif i == "(":
                        operators.append(i)
                    elif i == ")":
                        while operators and operators[-1] != "(":
                            postfix.append(operators.pop())
                        operators.pop()

                # Finalises the Postfix
                postfix += operators[::-1]

                # Stack used to evaluate postfix
                output = []

                # Evaluates Postfix and sets an Answer
                for i in postfix:
                    if re.match(r"\d+(?:\.\d+)?", i) is not None:
                        output.append(i)
                    
                    # Handles Functions
                    elif re.match(r"(sin|cos|tan|Log|Ln)", i) is not None:
                        # If there is no Number return an error
                        try:
                            num3 = output.pop()
                        except IndexError:
                            self.Answer.set("Syntax Error")
                            return



                        if i == "Log":
                            output.append(math.log10(float(num3)))
                        elif i == "Ln":
                            output.append(math.log(float(num3)))
                    
                    # Handles Basic Operators
                    else:
                        # If a Number is missing return an error
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
                            output.append(num1**(1/(num2)))
                        elif i == "^":
                            output.append(num2**num1)
                # Final Error Check
                if len(output) > 1:
                    self.Answer.set("Syntax Error")
                    return
                
                # Set answer and formatt
                Final = output[0]
                self.Answer.set(f"{Final:.8f}")





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

        self.Answerbox = Label(frame, textvariable= self.Answer, width=43, bg="White", anchor="e")
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

        frame.grid(row=0, column=0)
        return frame



    def Quadratic_Solver(self):
        pass


    def Simultaneous_Solver(self):
        pass




Calc = calculator()
Calc.run()


