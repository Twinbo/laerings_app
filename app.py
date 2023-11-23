#laering program 

import tkinter as LP
from tkinter import *
import random

K1 = None
F1 = None

def CreateWindow1():
    Add_Window1 = LP.Toplevel()
    Add_Window1.title('Addition')
    Add_Window1.geometry("800x500")

    def AddRandomTal():
        global K1
        global F1
        
        random_number.set(random.randint(1, 20))
        random_number2.set(random.randint(1, 20))

        #print("første nummer =", random_number)
        #print("anden nummer =", random_number2)

        SP.config(text=f"{random_number.get()} + {random_number2.get()}")

        E1.delete(0, LP.END)

        if K1 is not None:
            K1.destroy()
        if F1 is not None:
            F1.destroy()

    random_number = LP.StringVar()
    random_number2 = LP.StringVar()

    SP = LP.Label(Add_Window1, text="", font=('Arial',80))
    SP.pack(padx=10,pady=35)

    E1 = LP.Entry(Add_Window1,font=('Arial',44),width=8)
    E1.pack(padx=10,pady=10)

    def C1():
        global K1
        global F1

        user_svar = int(E1.get())
        print(user_svar)

        if user_svar == int(random_number.get()) + int(random_number2.get()):
            if F1 is not None:
                F1.destroy()

            K1 = LP.Label(Add_Window1, text="Korrekt, godt gået", font=('Arial',40))
            K1.pack(padx=10,pady=10)
            #print("Det er rigtigt, Godt gået1")

        else:
            F1 = LP.Label(Add_Window1, text=f"Forkert svar, det rigtige svar er {int(random_number.get()) + int(random_number2.get())}", font=('Arial',40))
            F1.pack(padx=10,pady=10)
            #print("Svaret er forkert, det rigtige svar var", int(random_number.get()) + int(random_number2.get()))
        
    B1 = LP.Button(Add_Window1, text="Tjek", font=('Arial', 28), command=C1).pack()
    B2 = LP.Button(Add_Window1, text="Næste", font=('Arial', 28),command=AddRandomTal).pack()
    
    AddRandomTal()
    
def CreateWindow2():
    Add_Window2 = LP.Toplevel()
    Add_Window2.title('Subtraktion')
    Add_Window2.geometry("800x500")

    def RT1():
        # random number 1
        random_number.set(random.randint(1, 20))
        print("første nummer =", random_number)
        # random number 2
        random_number2.set(random.randint(1, 20))
        print("anden nummer =", random_number2)

        SP1.config(text=f"{random_number.get()} - {random_number2.get()}")

        E2.delete(0, LP.END)
                        

    random_number = LP.StringVar()
    random_number2 = LP.StringVar() 

    SP1 = LP.Label(Add_Window2, text="", font=('Arial',44))
    SP1.pack(row=3)

    E2 = LP.Entry(Add_Window2,font=('Arial',44),width=8)
    E2.pack(padx=10,pady=10)

    def C2():
        
        user_svar = int(E2.get())
        print(user_svar)

        if user_svar == int(random_number.get()) - int(random_number2.get()):
            print("Det er rigtigt, Godt gået1")

        else:
            print("Svaret er forkert, det rigtige svar var", int(random_number.get()) - int(random_number2.get()))

    B1 = LP.Button(Add_Window2, text="Tjek", font=('Arial', 20), command=C2).pack(padx=10,pady=10)
    B2 = LP.Button(Add_Window2, text="Næste", font=('Arial', 20),command=RT1).pack(padx=10,pady=10)
    
    RT1()

def CreateWindow3():
    Add_Window3 = LP.Toplevel()
    Add_Window3.title('Multoplikation')
    Add_Window3.geometry("800x500")

    def RT2():
        # random number 1
        random_number.set(random.randint(1, 20))
        print("første nummer =", random_number)
        # random number 2
        random_number2.set(random.randint(1, 20))
        print("anden nummer =", random_number2)

        SP2.config(text=f"{random_number.get()} * {random_number2.get()}")

        E3.delete(0, LP.END)

    random_number = LP.StringVar()
    random_number2 = LP.StringVar() 

    SP2 = LP.Label(Add_Window3, text="", font=('Arial',44))
    SP2.pack(padx=10,pady=20)

    E3 = LP.Entry(Add_Window3,font=('Arial',44),width=8)
    E3.pack(padx=10,pady=10)

    def C3():
        user_svar = int(E3.get())
        print(user_svar)

        if user_svar == int(random_number.get()) * int(random_number2.get()):
            print("Det er rigtigt, Godt gået1")

        else:
            print("Svaret er forkert, det rigtige svar var", int(random_number.get()) * int(random_number2.get()))

    B1 = LP.Button(Add_Window3, text="Tjek", font=('Arial', 20), command=C3).pack(padx=10,pady=10)
    B2 = LP.Button(Add_Window3, text="Næste", font=('Arial', 20),command=RT2).pack(padx=10,pady=10)
    
    RT2()

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


