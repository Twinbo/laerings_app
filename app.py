#laering program 

import tkinter as LP
from tkinter import *
import random

def CreateWindow1():
    Add_Window1 = LP.Toplevel()
    Add_Window1.title('Addition')
    Add_Window1.geometry("800x500")

    def RT():
        # random number 1
        random_number.set(random.randint(1, 20))
        print("første nummer =", random_number)
        # random number 2
        random_number2.set(random.randint(1, 20))
        print("anden nummer =", random_number2)

        SP.config(text=f"{random_number.get()} + {random_number2.get()}")

        E1.delete(0, LP.END)

    random_number = LP.StringVar()
    random_number2 = LP.StringVar() 

    SP = LP.Label(Add_Window1, text="", font=('Arial',44))
    SP.pack(padx=10,pady=20)

    E1 = LP.Entry(Add_Window1,font=('Arial',44),width=8)
    E1.pack(padx=10,pady=10)

    def C1():
        user_svar = int(E1.get())
        print(user_svar)

        if user_svar == int(random_number.get()) + int(random_number2.get()):
            print("Det er rigtigt, Godt gået1")

        else:
            print("Svaret er forkert, det rigtige svar var", int(random_number.get()) + int(random_number2.get()))

    B1 = LP.Button(Add_Window1, text="Tjek", font=('Arial', 20), command=C1).pack(padx=10,pady=10)
    B2 = LP.Button(Add_Window1, text="Næste", font=('Arial', 20),command=RT).pack(padx=10,pady=10)
    
    RT()
    
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

        self.knapFrame = LP.Frame(self.root)
        self.knapFrame.columnconfigure(0,weight=1)
        self.knapFrame.columnconfigure(1,weight=1)
        self.knapFrame.columnconfigure(2,weight=1)
        
        self.knapAdd = LP.Button(self.knapFrame, text="Addition", width=10,font=('Arial',28), command = lambda: [CreateWindow1()])
        self.knapAdd.grid(row=0,column=0,padx=1)

        self.knapMin = LP.Button(self.knapFrame, text="Subtraktion", width=10,font=('Arial',28),command = CreateWindow2)
        self.knapMin.grid(row=0,column=1,padx=1)

        self.knapGan = LP.Button(self.knapFrame, text="Multiplikation", width=10,font=('Arial',28),command = CreateWindow3)
        self.knapGan.grid(row=0,column=2,padx=1)

        self.knapFrame.pack(padx=10,pady=20)

        self.root.mainloop() 

LPapp()


