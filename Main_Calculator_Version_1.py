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
                pass
            case 2,1:
                self.Equationbox.insert("insert","\u00B2")
            case 2,2:
                self.Equationbox.insert("insert","Log")
            case 2,3:
                pass
            case 2,4:
                pass
            case 3,0:
                self.Equationbox.insert("insert","\u00B2\u221A")
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
                equation = self.Equationbox.get()
                equation_f = list(str(equation))
                
                for i in equation_f:
                    position = equation_f.index(i)
                    if i == "X":
                        equation_f[equation_f.index(i)] = "*"


                    elif i == "÷":
                        equation_f[equation_f.index(i)] = "/"


                    elif i == "π":
                        equation_f[equation_f.index(i)] = str(math.pi)


                    elif i == "e":
                        equation_f[equation_f.index(i)] = str(math.e)


                    elif i =="L":
                        print(i)
                        if equation_f[equation_f.index(i)+1] == "o":
                            loged = ""
                            for k in equation_f[equation_f.index(i) + 3: len(equation_f)]:
                                if k.isdigit()== True:
                                    loged += k
                                else:
                                    break
                            print(loged)
                            del equation_f[equation_f.index(i)+1:(equation_f.index(i)+3+len(loged))]
                            equation_f[equation_f.index(i)] = str(math.log10(int(loged)))
                        elif equation_f[equation_f.index(i)+1] == "n":
                            loged = ""
                            for k in equation_f[equation_f.index(i) + 2: len(equation_f)]:
                                if k.isdigit()== True:
                                    loged += k
                                else:
                                    break
                            print(loged)
                            del equation_f[equation_f.index(i)+1:(equation_f.index(i)+2+len(loged))]
                            equation_f[equation_f.index(i)] = str(math.log(int(loged)))
                    elif i == "\u00B2":
                        equation_f[equation_f.index(i)] = "**2"


                    elif i == "^":
                        powered = ""
                        for k in equation_f[equation_f.index(i) + 1: len(equation_f)]:
                                if k.isdigit()== True:
                                    powered += k
                                else:
                                    break
                        del equation_f[equation_f.index(i)+1:(equation_f.index(i)+1+len(powered))]
                        equation_f[equation_f.index(i)] = f"**{powered}"        


                    elif i == "\u221A":
                        if equation_f[equation_f.index(i)-1] == "\u00B2":
                            squared = ""
                            for k in equation_f[equation_f.index(i) + 1: len(equation_f)]:
                                    if k.isdigit()== True:
                                        squared += k
                                    else:
                                        break
                            del equation_f[equation_f.index(i)+1:(equation_f.index(i)+1+len(squared))]
                            equation_f[equation_f.index(i)] = str(math.sqrt(powered))





                equation_f = "".join(equation_f)

                print(equation_f)
                self.Answer.set(str(eval(equation_f)))

            case 9,0:
                self.Equationbox.insert("insert","0")
            case 9,1:
                pass
    
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


