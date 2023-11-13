#laering program 

import tkinter as LP
from tkinter import ttk
import random

def CreateWindow1():
    Add_Window1 = LP.Toplevel()
    Add_Window1.title('Addition')
    Add_Window1.geometry("800x500")
    LP.Label(Add_Window1,text="Plus regnestykker", font=('Arial',24 )).pack(padx=10,pady=60)
    LP.Text(Add_Window1, height=1, width=30,font=('Arial',16)).pack(pady=10)
  
    # random number 1
    random_number = random.randint(1, 20)
    print("første nummer =", random_number)

    # random number 2
    random_number2 = random.randint(1, 20)
    print("anden nummer =", random_number2)

    print()

    print("Plus stykke", random_number, "+", random_number2)
    user_answer = int(input())
    if user_answer == random_number + random_number2:
         print("Det er rigtigt, Godt gået")
    else:
        print("Prøv igen")
        user_answer = int(input())
        if user_answer == random_number + random_number2:
            print("Det er rigtigt, Godt gået")
        else:
            print("Svaret er forkert, det rigtige svar var", random_number + random_number2)
    

def CreateWindow2():
    Add_Window2 = LP.Toplevel()
    Add_Window2.title('Subtraktion')
    Add_Window2.geometry("800x500")

def CreateWindow3():
    Add_Window3 = LP.Toplevel()
    Add_Window3.title('Multoplikation')
    Add_Window3.geometry("800x500")

class   LPapp:

    def __init__(self):

        self.root = LP.Tk()

        self.root.geometry("800x500")
        self.root.title("MatLæring")

        self.label1 = LP.Label(self.root, text="Matematik", font=('Arial',44))
        self.label1.pack(padx=10,pady=60)

        self.label = LP.Label(self.root, text="Vælg kategori", font=('Arial',24))
        self.label.pack(padx=10,pady=10)

        #self.textbox = LP.Text(self.root, height=1, width=30,font=('Arial',16))
        #self.textbox.pack(pady=10)

        self.knapFrame = LP.Frame(self.root)
        self.knapFrame.columnconfigure(0,weight=1)
        self.knapFrame.columnconfigure(1,weight=1)
        self.knapFrame.columnconfigure(2,weight=1)
        
        self.knapAdd = LP.Button(self.knapFrame, text="Addition", width=10,font=('Arial',28), command = CreateWindow1)
        self.knapAdd.grid(row=0,column=0,padx=1)

        self.knapMin = LP.Button(self.knapFrame, text="Subtraktion", width=10,font=('Arial',28),command = CreateWindow2)
        self.knapMin.grid(row=0,column=1,padx=1)

        self.knapGan = LP.Button(self.knapFrame, text="Multiplikation", width=10,font=('Arial',28),command = CreateWindow3)
        self.knapGan.grid(row=0,column=2,padx=1)

        self.knapFrame.pack(padx=10,pady=20)

        self.root.mainloop() 

#def lukProgram(self):
    #if 

LPapp()

class addt:

    def adtn(self):

        self.Addtiontext = LP.Text(self.root, height=1, width=30,font=('Arial',16))
        self.Addtiontext.pack(pady=10)
        
        
addt()
