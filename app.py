#laering program 

import tkinter as LP
from tkinter import *
import random

K1 = None
F1 = None

def CreateWindow1(IV1Value,IV2Value):
    Add_Window1 = LP.Toplevel()
    Add_Window1.title('Addition')
    Add_Window1.geometry("800x600")
    print(IV1Value)
    print(IV2Value)

    def RandomTal():
        global K1
        global F1
        
        random_number.set(random.randint(IV1Value, IV2Value))
        random_number2.set(random.randint(IV1Value, IV2Value))

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
    B2 = LP.Button(Add_Window1, text="Næste", font=('Arial', 28),command=RandomTal).pack()
    
    RandomTal()
    
def CreateWindow2(IV1Value,IV2Value):
    Add_Window2 = LP.Toplevel()
    Add_Window2.title('Subtraktion')
    Add_Window2.geometry("800x600")

    print(IV1Value)
    print(IV2Value)

    def RandomTal():
        global K1
        global F1
        
        random_number.set(random.randint(IV1Value, IV2Value))
        random_number2.set(random.randint(IV1Value, IV2Value))

        #print("første nummer =", random_number)
        #print("anden nummer =", random_number2)

        SP.config(text=f"{random_number.get()} - {random_number2.get()}")

        E1.delete(0, LP.END)

        if K1 is not None:
            K1.destroy()
        if F1 is not None:
            F1.destroy()

    random_number = LP.StringVar()
    random_number2 = LP.StringVar()

    SP = LP.Label(Add_Window2, text="", font=('Arial',80))
    SP.pack(padx=10,pady=35)

    E1 = LP.Entry(Add_Window2,font=('Arial',44),width=8)
    E1.pack(padx=10,pady=10)

    def C1():
        global K1
        global F1

        user_svar = int(E1.get())
        print(user_svar)

        if user_svar == int(random_number.get()) - int(random_number2.get()):
            if F1 is not None:
                F1.destroy()

            K1 = LP.Label(Add_Window2, text="Korrekt, godt gået", font=('Arial',40))
            K1.pack(padx=10,pady=10)
            #print("Det er rigtigt, Godt gået1")

        else:
            F1 = LP.Label(Add_Window2, text=f"Forkert svar, det rigtige svar er {int(random_number.get()) - int(random_number2.get())}", font=('Arial',40))
            F1.pack(padx=10,pady=10)
            #print("Svaret er forkert, det rigtige svar var", int(random_number.get()) + int(random_number2.get()))
        
    B1 = LP.Button(Add_Window2, text="Tjek", font=('Arial', 28), command=C1).pack()
    B2 = LP.Button(Add_Window2, text="Næste", font=('Arial', 28),command=RandomTal).pack()
    
    RandomTal()

def CreateWindow3(IV1Value,IV2Value):
    Add_Window3 = LP.Toplevel()
    Add_Window3.title('Multoplikation')
    Add_Window3.geometry("800x600")

    print(IV1Value)
    print(IV2Value)

    def RandomTal():
        global K1
        global F1
        
        random_number.set(random.randint(IV1Value, IV2Value))
        random_number2.set(random.randint(IV1Value, IV2Value))

        #print("første nummer =", random_number)
        #print("anden nummer =", random_number2)

        SP.config(text=f"{random_number.get()} * {random_number2.get()}")

        E1.delete(0, LP.END)

        if K1 is not None:
            K1.destroy()
        if F1 is not None:
            F1.destroy()

    random_number = LP.StringVar()
    random_number2 = LP.StringVar()

    SP = LP.Label(Add_Window3, text="", font=('Arial',80))
    SP.pack(padx=10,pady=35)

    E1 = LP.Entry(Add_Window3,font=('Arial',44),width=8)
    E1.pack(padx=10,pady=10)

    def C1():
        global K1
        global F1

        user_svar = int(E1.get())
        print(user_svar)

        if user_svar == int(random_number.get()) * int(random_number2.get()):
            if F1 is not None:
                F1.destroy()

            K1 = LP.Label(Add_Window3, text="Korrekt, godt gået", font=('Arial',40))
            K1.pack(padx=10,pady=10)
            #print("Det er rigtigt, Godt gået1")

        else:
            F1 = LP.Label(Add_Window3, text=f"Forkert svar, det rigtige svar er {int(random_number.get()) * int(random_number2.get())}", font=('Arial',40))
            F1.pack(padx=10,pady=10)
            #print("Svaret er forkert, det rigtige svar var", int(random_number.get()) + int(random_number2.get()))
        
    B1 = LP.Button(Add_Window3, text="Tjek", font=('Arial', 28), command=C1).pack()
    B2 = LP.Button(Add_Window3, text="Næste", font=('Arial', 28),command=RandomTal).pack()
    
    RandomTal()

class   LPapp:

    def __init__(self):

        self.root = LP.Tk()

        self.root.geometry("800x600")
        self.root.title("MatLæring")

        self.label1 = LP.Label(self.root, text="Matematik", font=('Arial',44))
        self.label1.pack(padx=10,pady=60)

        self.label = LP.Label(self.root, text="Vælg kategori", font=('Arial',24))
        self.label.pack(padx=10,pady=10)

        self.knapFrame = LP.Frame(self.root)
        self.knapFrame.columnconfigure(0,weight=1)
        self.knapFrame.columnconfigure(1,weight=1)
        self.knapFrame.columnconfigure(2,weight=1)
        
        
        self.knapAdd = LP.Button(self.knapFrame, text="Addition", width=10,font=('Arial',28), command = lambda: [self.IV1ValueGet(),self.IV2ValueGet(), CreateWindow1(self.IV1Value,self.IV2Value)])
        self.knapAdd.grid(row=0,column=0,padx=1)

        self.knapMin = LP.Button(self.knapFrame, text="Subtraktion", width=10,font=('Arial',28),command = lambda: [self.IV1ValueGet(),self.IV2ValueGet(), CreateWindow2(self.IV1Value,self.IV2Value)])
        self.knapMin.grid(row=0,column=1,padx=1)

        self.knapGan = LP.Button(self.knapFrame, text="Multiplikation", width=10,font=('Arial',28),command = lambda: [self.IV1ValueGet(),self.IV2ValueGet(), CreateWindow3(self.IV1Value,self.IV2Value)])
        self.knapGan.grid(row=0,column=2,padx=1)

        self.knapFrame.pack(padx=10,pady=20)

        self.IVFrame = LP.Frame(self.root)
        self.IVFrame.columnconfigure(0,weight=1)
        self.IVFrame.columnconfigure(1,weight=1)
        self.IVFrame.columnconfigure(2,weight=1)
       


        self.IVTal = LP.Label(self.IVFrame, text="Indsæt tal", font=('Arial',20))
        self.IVTal.grid(row=0,column=1,padx=1)

        self.IV1Label = LP.Label(self.IVFrame, text="Mininum:", font=('Arial',20))
        self.IV1Label.grid(row=1,column=0,padx=1)

        self.IV1 = LP.Entry(self.IVFrame,font=('Arial',20),width=8)
        self.IV1.grid(row=1,column=1,padx=1)


        self.IV2Label = LP.Label(self.IVFrame, text="Maksimum:", font=('Arial',20))
        self.IV2Label.grid(row=2,column=0,padx=1)

        self.IV2 = LP.Entry(self.IVFrame,font=('Arial',20),width=8)
        self.IV2.grid(row=2,column=1,padx=1)

        self.IVFrame.pack(padx=10,pady=20)

        

        self.root.mainloop() 

    def IV1ValueGet(self):
        self.IV1Value = int(self.IV1.get())

    def IV2ValueGet(self):
        self.IV2Value = int(self.IV2.get())

LPapp()


