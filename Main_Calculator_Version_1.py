"""
GUI for main Calculator.
This version will include the GUI of the main calcultor as well as the function where the functional development will occur.
It will use for loops to create buttons and have a method of differentaiting which button is which, to allow them to preform their function.
18/07/25
"""


from tkinter import *
import math

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
            "10": "\u221A",
            "11": "x\u00B2",
            "12": "Log",
            "13": "Menu",
            "14": "F<->D",
            "20": "\u00B2\u221A",
            "21": "x\u02E3",
            "22": "Ln",
            "23": "(",
            "24": ")",
            "30": "sin",
            "31": "cos",
            "32": "tan",
            "33": "π",
            "34": "e",
            "40": "sin\u207B\u00B9",
            "41": "cos\u207B\u00B9",
            "42": "tan\u207B\u00B9",
            "43": "x/x",
            "44": "AC",
            "50": "1",
            "51": "2",
            "52": "3",
            "53": "X",
            "54": "÷",
            "60": "4",
            "61": "5",
            "62": "6",
            "63": "+",
            "64": "-",
            "70": "7",
            "71": "8",
            "72": "9",
            "73": "DEL",
            "74": "EXE",
            "80": "0",
            "81": "."}

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
            case 1,0:
                pass
            case 1,1:
                pass
            case 1,2:
                pass
            case 1,3:
                pass
            case 1,4:
                pass
            case 2,0:
                pass
            case 2,1:
                pass
            case 2,2:
                pass
            case 2,3:
                pass
            case 2,4:
                pass
            case 3,0:
                pass
            case 3,1:
                pass
            case 3,2:
                pass
            case 3,3:
                pass
            case 3,4:
                pass
            case 4,0:
                pass
            case 4,1:
                pass
            case 4,2:
                pass
            case 4,3:
                pass
            case 4,4:
                pass
            case 5,0:
                self.Equationbox.insert("insert","1")
            case 5,1:
                self.Equationbox.insert("insert","2")
            case 5,2:
                self.Equationbox.insert("insert","3")
            case 5,3:
                self.Equationbox.insert("insert","X")
            case 5,4:
                self.Equationbox.insert("insert","÷")
            case 6,0:
                self.Equationbox.insert("insert","4")
            case 6,1:
                self.Equationbox.insert("insert","5")
            case 6,2:
                self.Equationbox.insert("insert","6")
            case 6,3:
                self.Equationbox.insert("insert","+")
            case 6,4:
                self.Equationbox.insert("insert","-")
            case 7,0:
                self.Equationbox.insert("insert","7")
            case 7,1:
                self.Equationbox.insert("insert","8")
            case 7,2:
                self.Equationbox.insert("insert","9")
            case 7,3:
                self.Equationbox.delete(INSERT + "-1c")
            case 7,4:
                equation = self.Equationbox.get(1.0, "1.0 lineend")
                equation_f = list(str(equation))
                for i in equation_f:
                    if i == "X":
                        equation_f[equation_f.index(i)] = "*"
                    elif i == "÷":
                        equation_f[equation_f.index(i)] = "/"
                equation_f = "".join(equation_f)
                
                
                self.Equationbox.insert("4.end", eval(equation_f))
            case 8,0:
                pass
            case 8,1:
                pass
    
    # The GUI of the main calculator
    def Main_Calculator(self):
        # Defining the frames properties
        frame = Frame(self.container)
        frame.rowconfigure([0,1,2,3,4,5,6,7,8], weight=1, minsize=40)
        frame.columnconfigure([0,1,2,3,4], weight=1, minsize=60)

        # Where the equation will be written
        self.Equationbox = Text(frame, width=40, height=4, wrap="none")
        self.Equationbox.grid(row=0, columnspan=5,pady=10, padx=5)
        # Textbox lines are generated dynamicaly so to have them exist when I want to add the answer I need to create them
        self.Equationbox.insert(2.0, "\n")
        self.Equationbox.insert(3.0, "\n")
        self.Equationbox.insert(4.0, "\n")
        self.Equationbox.mark_set("insert", 1.0)

        # Creates the main mass of buttons
        for i in range(1, 5):
            for j in range(0,5):

                # Creates the unqiue identifer for that button for its label.
                Name = str(i) + str(j)
                
                self.CenterButtons = Button(frame, text=self.Labels[Name], width=5, command=lambda i=i, j=j: self.Operators(i, j))
                self.CenterButtons.grid(row=i, column=j, pady=3)
        

        # Creates the Side buttons
        for i in range(5,8):
            for j in range(3,5):
                Name = str(i) + str(j)
                self.RightButtons = Button(frame, text=self.Labels[Name], width=5, command=lambda i=i, j=j: self.Operators(i, j))
                self.RightButtons.grid(row=i, column=j, pady=3)

        
        # Creates the Numberpad
        for i in range(5,8):
            for j in range(0,3):
                Name = str(i) + str(j)
                self.NumButtons = Button(frame, text=self.Labels[Name], width=5, height=2, command=lambda i=i, j=j: self.Operators(i, j))
                self.NumButtons.grid(row=i, column=j, pady=3)

        # Creates the two buttons beneath the  numberpad.
        for i in range(8,9):
            for j in range(0,2):
                Name = str(i) + str(j)
                self.PlaceButtons = Button(frame, text=self.Labels[Name], width=5, command=lambda i=i, j=j: self.Operators(i, j))
                self.PlaceButtons.grid(row=i, column=j, pady=3)

        frame.grid(row=0, column=0)
        return frame



    def Quadratic_Solver(self):
        pass


    def Simultaneous_Solver(self):
        pass




Calc = calculator()
Calc.run()


