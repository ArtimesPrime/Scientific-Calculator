"""
Final Calculator
Non-Styled Version
Contains a dynamic fully functioning scientfic Calculator and Quadratic Solver
29/08/2025
By Ethan Beale
"""


from tkinter import *  # Creates GUI
import math  # Performs more advanced Math operations
import re  # Allows for regex patterns and search methods


# The Class where all the calculator will be contained.
class Calculator:

    # Initializing and defining the properties of the program.
    def __init__(self):
        self.root = Tk()
        self.root.title("Calculator")
        self.container = Frame(self.root)
        self.container.grid(row=0, column=0, sticky=NSEW)

        # All Regex Patterns
        self.TOKEN_PATTERN = re.compile(r"\d+(?:\.\d+)?"
                                        r"|e|\u221A|π|"
                                        r"(?:sin|cos|tan)(?:\u207B\u00B9)?"
                                        r"|Log|Ln|[-+÷X/^()]")

        self.NUMBER_PATTERN = r"-?\d+(?:\.\d+)?"
        self.FUNCTION_PATTERN = r"((?:sin|cos|tan)(?:\u207B\u00B9)?|Log|Ln|u)"

        # Operators/Functions
        self.OPERATIONS = ["+", "-", "÷", "X",
                           "^", "\u221A",
                           "Log", "Ln",
                           "sin", "cos", "tan",
                           "sin\u207B\u00B9",
                           "cos\u207B\u00B9",
                           "tan\u207B\u00B9"]

        # Dictionary of the unique identifier of each button and its label.
        self.LABELS = {
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

        self.answer = StringVar()
        self.answer.set("")
        self.quad = StringVar()
        self.quad.set("")
        self.entry = None

        # Creates the dictionary of the frames and creates the frames
        self.frames = {}
        self.frames["Main Calculator"] = self.main_calculator()
        self.frames["Quadratic Solver"] = self.quadratic_solver()
        self.frames["Simultaneous Solver"] = self.simultaneous_solver()
        self.frames["Menu"] = self.menu()

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
        self.entry = None
    # Decides where buttons enter Text

    def set_entry(self, event):
        self.entry = event.widget

    # Solves Equations
    def solve(self, equation):
        # Creates a list from the equation that breaks at relevant segements.
        tokens = re.findall(self.TOKEN_PATTERN, equation)
        # Facilitates Order of operations
        priority = {"+": 1, "-": 1, "÷": 2, "X": 2,
                    "^": 3, "\u221A": 3,
                    "Log": 4, "Ln": 4,
                    "sin": 4, "cos": 4, "tan": 4,
                    "sin\u207B\u00B9": 4,
                    "cos\u207B\u00B9": 4,
                    "tan\u207B\u00B9": 4,
                    "u": 5
                    }
        # Postfix is output of the next block
        postfix = []
        # Stack that allows operators to be handled correctly.
        operators = []
        # Used to decide if a minus is uranary or not.
        Last = None

        # Turns Infix into Postifx
        for i in tokens:
            if re.match(self.NUMBER_PATTERN, i) is not None:
                postfix.append(i)
            # Decides if a minus is unary or not
            elif (i == "-" and
                  (Last == None or Last in {"^", "(", "+", "-", "X", "÷",
                                            "\u00B2\u221A", "\u221A"})):
                operators.append("u")

            elif i in self.OPERATIONS:
                # This makes sure the operators are in the correct order.
                while (operators and operators[-1] in priority and
                       priority[operators[-1]] >= priority[i]):
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
                print(postfix)
            elif i == ")":
                while operators and operators[-1] != "(":
                    postfix.append(operators.pop())
                    print(postfix)
                operators.pop()
            Last = i

        # Finalises the Postfix
        postfix += operators[::-1]
        print(postfix)
        # Stack used to evaluate postfix
        output = []

        # Evaluates Postfix and returns an Answer
        for i in postfix:
            print(output)
            if re.match(self.NUMBER_PATTERN, i) is not None:
                output.append(i)
            # Handles Functions
            elif re.match(self.FUNCTION_PATTERN, i) is not None:
                # If there is no Number return an error
                try:
                    num3 = output.pop()
                except IndexError:
                    self.answer.set("Syntax Error")
                    return
                # If outside domain Return error.
                try:
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
                        output.append(math.asin(float(num3)))

                    elif i == "cos\u207B\u00B9":
                        output.append(math.acos(float(num3)))

                    elif i == "tan\u207B\u00B9":
                        output.append(math.atan(float(num3)))

                    elif i == "u":
                        output.append(-float(num3))
                except ValueError:
                    self.answer.set("Math Domain Error")
            # Handles Basic Operators
            else:
                print(output)
                try:
                    num1 = float(output.pop())
                    num2 = float(output.pop())
                except IndexError:
                    self.answer.set("Syntax Error")
                    return
                if i == "+":
                    output.append(num2+num1)
                elif i == "-":
                    output.append(num2-num1)
                elif i == "X":
                    output.append(num2*num1)
                elif i == "÷":
                    # Prevents Divide by 0 Error
                    try:
                        output.append(num2/num1)
                    except ZeroDivisionError:
                        self.answer.set("Cant Divide by 0")
                        return
                elif i == "\u221A":
                    # Prevents Negative roots
                    if num1 < 0:
                        self.answer.set(
                            "Math Error: Complex Domain Not Supported")
                        return
                    output.append(num1**(1/(num2)))
                elif i == "^":
                    # Prevents Negative roots
                    try:
                        output.append(math.pow(num2, num1))
                    except ValueError:
                        self.answer.set(
                            "Math Error: Complex Domain not Supported.")
                        return
        # Final Error Check
        if len(output) > 1:
            self.answer.set("Syntax Error")
            return

        Final = output[0]

        # Makes Sure Output is within Bounduary
        if float(Final) > 0:
            if float(Final) >= 10**16 or float(Final) <= 10**-16:
                self.answer.set("Math Error")
                return
        else:
            if float(Final) < -10**16:
                self.answer.set("Math Error")
                return
        # Return answer
        return (Final)

    # Solves Quadratics
    def quadratic_evaluation(self):
        # If a root cant be collected or turned into a float return an error
        try:
            # Solve allows equations to be entered
            a = float(self.solve(self.coefficients["a"].get()))
            b = float(self.solve(self.coefficients["b"].get()))
            c = float(self.solve(self.coefficients["c"].get()))
        except Exception:
            self.quad.set("Enter valid numbers for a, b, c")
            return

        # Determines if there are no roots
        try:
            dis = math.sqrt((b**2) - (4*a*c))
        except ValueError:
            self.quad.set("No Real Roots")
            return

        # Outputs Roots
        root1 = (-b + dis) / (2*a)
        root2 = (-b - dis) / (2*a)
        if root1 != root2:
            self.quad.set(f"X = {root1} or X = {root2}")
        else:
            self.quad.set(f"X = {root1}")

    # Contains the operations preform by each button
    def operators(self, r, c):
        # Sets Where to enter.
        if self.entry is not None:
            entrypoint = self.entry
        else:
            entrypoint = self.Equationbox
        match(r, c):
            case 2, 0:
                # Every Line in this formatt does the same thing.
                # Append to equationbox.
                entrypoint.insert("insert", "( )\u221A")
            case 2, 1:
                entrypoint.insert("insert", "^2")
            case 2, 2:
                entrypoint.insert("insert", "Log()")
            case 2, 3:
                self.show_frame("Menu")
            case 2, 4:
                pass
            case 3, 0:
                entrypoint.insert("insert", "(2)\u221A")
            case 3, 1:
                entrypoint.insert("insert", "^")
            case 3, 2:
                entrypoint.insert("insert", "Ln()")
            case 3, 3:
                entrypoint.insert("insert", "(")
            case 3, 4:
                entrypoint.insert("insert", ")")
            case 4, 0:
                entrypoint.insert("insert", "sin()")
            case 4, 1:
                entrypoint.insert("insert", "cos()")
            case 4, 2:
                entrypoint.insert("insert", "tan()")
            case 4, 3:
                entrypoint.insert("insert", "π")
            case 4, 4:
                entrypoint.insert("insert", "e")
            case 5, 0:
                entrypoint.insert("insert", "sin\u207B\u00B9()")
            case 5, 1:
                entrypoint.insert("insert", "cos\u207B\u00B9()")
            case 5, 2:
                entrypoint.insert("insert", "tan\u207B\u00B9()")
            case 5, 3:
                pass
            case 5, 4:
                # Clears Equation and Answer box
                entrypoint.delete(0, END)
                self.answer.set("")
            case 6, 0:
                entrypoint.insert("insert", "1")
            case 6, 1:
                entrypoint.insert("insert", "2")
            case 6, 2:
                entrypoint.insert("insert", "3")
            case 6, 3:
                entrypoint.insert("insert", "X")
            case 6, 4:
                entrypoint.insert("insert", "÷")
            case 7, 0:
                entrypoint.insert("insert", "4")
            case 7, 1:
                entrypoint.insert("insert", "5")
            case 7, 2:
                entrypoint.insert("insert", "6")
            case 7, 3:
                entrypoint.insert("insert", "+")
            case 7, 4:
                entrypoint.insert("insert", "-")
            case 8, 0:
                entrypoint.insert("insert", "7")
            case 8, 1:
                entrypoint.insert("insert", "8")
            case 8, 2:
                entrypoint.insert("insert", "9")
            case 8, 3:
                # Deletes based on where the text pointer is.
                pos = entrypoint.index(INSERT)
                entrypoint.delete(pos - 1)

            case 8, 4:
                # Preforms Calculation
                final_answer = (self.solve(entrypoint.get()))
                if final_answer != None:
                    self.answer.set(final_answer)

            case 9, 0:
                entrypoint.insert("insert", "0")
            case 9, 1:
                entrypoint.insert("insert", ".")

    # The GUI of the main calculator

    def main_calculator(self):
        # Defining the frames properties
        frame = Frame(self.container)
        frame.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                           weight=1, minsize=30)
        frame.columnconfigure([0, 1, 2, 3, 4], weight=1, minsize=60)

        # Where the equation will be written
        self.Equationbox = Entry(frame, width=50,)
        self.Equationbox.grid(row=0, columnspan=5,
                              padx=5, pady=0, sticky="NSEW")

        # Contains the Answer
        self.Answerbox = Label(
            frame, textvariable=self.answer, bg="White", anchor="e")
        self.Answerbox.grid(row=1, columnspan=5, padx=5,
                            pady=0,  sticky="NSEW")

        # Creates the main mass of buttons
        for i in range(2, 6):
            for j in range(0, 5):
                self.CenterButtons = Button(frame, text=self.LABELS[(
                    i, j)], width=5,
                    command=lambda i=i, j=j: self.operators(i, j))
                self.CenterButtons.grid(row=i, column=j, pady=6)

        # Creates the Side buttons
        for i in range(6, 9):
            for j in range(3, 5):
                self.RightButtons = Button(frame, text=self.LABELS[(
                    i, j)], width=5,
                    command=lambda i=i, j=j: self.operators(i, j))
                self.RightButtons.grid(row=i, column=j, pady=3)

        # Creates the Numberpad
        for i in range(6, 9):
            for j in range(0, 3):
                self.NumButtons = Button(frame, text=self.LABELS[(
                    i, j)],
                    width=5, height=2,
                    command=lambda i=i, j=j: self.operators(i, j))
                self.NumButtons.grid(row=i, column=j, pady=3)

        # Creates the two buttons beneath the  numberpad.
        for i in range(9, 10):
            for j in range(0, 2):
                self.PlaceButtons = Button(frame, text=self.LABELS[(
                    i, j)], width=5,
                    command=lambda i=i, j=j: self.operators(i, j))
                self.PlaceButtons.grid(row=i, column=j, pady=3)

        frame.grid(row=0, column=0, sticky=NSEW)
        return frame

    # GUI of Menu
    def menu(self):
        # Defining the frames properties
        frame = Frame(self.container)
        frame.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                           weight=1, minsize=30)
        frame.columnconfigure([0], weight=1, minsize=300)

        # Title of Menu
        self.MenuTitle = Label(frame, text="Menu",
                               font="Verdana 20 bold")
        self.MenuTitle.grid(row=0, sticky=NSEW)

        # Main Calculator Button
        self.MainButton = Button(
            frame, text="Main Calculator", height=3,
            command=lambda: self.show_frame("Main Calculator"))
        self.MainButton.grid(row=2, sticky=NSEW)

        # Quadratic Calculator Button
        self.QuadraticButton = Button(
            frame, text="Quadratic Solver", height=3,
            command=lambda: self.show_frame("Quadratic Solver"))
        self.QuadraticButton.grid(row=4, sticky=NSEW)

        # simultaneous Calculator Button
        # (Though Defunct kept as serves a purpose in future proofing.)
        self.SimultaneousButton = Button(
            frame, text="Simultaneous Solver", height=3,
            command=lambda: self.show_frame("Simultaneous Solver"))
        self.SimultaneousButton.grid(row=6, sticky=NSEW)

        frame.grid(row=0, column=0, sticky=NSEW)
        return frame

    # GUI of Quadratic Solver
    def quadratic_solver(self):
        # Defining the frames properties
        frame = Frame(self.container)
        frame.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                           weight=1, minsize=30)
        frame.columnconfigure([0, 1, 2, 3, 4], weight=1, minsize=30)
        self.coefficients = {}

        labels = ["a", "b", "c"]
        for i, lbl in enumerate(labels):
            self.coefficients[lbl] = Entry(frame, width=9)
            self.coefficients[lbl].grid(row=0, column=i*2,
                                        padx=3, sticky="NEW")
            self.coefficients[lbl].bind("<FocusIn>", self.set_entry)

        self.QuadAnswerbox = Label(
            frame, textvariable=self.quad,
            bg="White", anchor="w")
        self.QuadAnswerbox.grid(row=1, columnspan=5,
                                padx=5, pady=0,  sticky="NSEW")

        # Creates the main mass of buttons
        for i in range(2, 6):
            for j in range(0, 5):
                self.CenterButtons = Button(
                    frame, text=self.LABELS[(i, j)],
                    width=5,
                    command=lambda i=i, j=j: self.operators(i, j))
                self.CenterButtons.grid(row=i, column=j, pady=6)

        # Creates the Side buttons
        for i in range(6, 9):
            for j in range(3, 5):
                self.RightButtons = Button(
                    frame, text=self.LABELS[(i, j)],
                    width=5,
                    command=lambda i=i, j=j: self.operators(i, j))
                self.RightButtons.grid(row=i, column=j, pady=3)

        # Overwrites Main EXE box when on Quad
        self.NEWEXEButton = Button(
            frame, text="EXE",
            width=5,
            command=lambda: self.quadratic_evaluation())
        self.NEWEXEButton.grid(row=8, column=4, pady=3)

        # Creates the Numberpad
        for i in range(6, 9):
            for j in range(0, 3):
                self.NumButtons = Button(
                    frame, text=self.LABELS[(i, j)],
                    width=5, height=2,
                    command=lambda i=i, j=j: self.operators(i, j))
                self.NumButtons.grid(row=i, column=j, pady=3)

        # Creates the two buttons beneath the  numberpad.
        for i in range(9, 10):
            for j in range(0, 2):
                self.PlaceButtons = Button(
                    frame, text=self.LABELS[(i, j)],
                    width=5,
                    command=lambda i=i, j=j: self.operators(i, j))
                self.PlaceButtons.grid(row=i, column=j, pady=3)

        frame.grid(row=0, column=0, sticky=NSEW)
        return frame

    def simultaneous_solver(self):
        pass


Calc = Calculator()
Calc.run()
