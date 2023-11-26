#laering program 

import tkinter as LP
from tkinter import *
import random

class   LPapp:

    def __init__(self):

        self.root = LP.Tk()

        self.root.geometry("800x450")
        self.root.title("MatMA")

        self.label1 = LP.Label(self.root, text="MatMa - Matematik", font=('Arial',44))
        self.label1.pack(padx=10,pady=40)

        self.label = LP.Label(self.root, text="Vælg kategori", font=('Arial',24))
        self.label.pack(padx=10,pady=10)

        self.knapFrame = LP.Frame(self.root)
        self.knapFrame.columnconfigure(0,weight=1)
        self.knapFrame.columnconfigure(1,weight=1)
        self.knapFrame.columnconfigure(2,weight=1)
        self.knapFrame.columnconfigure(3,weight=1)
        self.knapFrame.columnconfigure(4,weight=1)
        
        self.knapAdd = LP.Button(self.knapFrame, text="Addition", width=10,font=('Arial',28), command = lambda: [self.IV1ValueGet(),self.IV2ValueGet(), self.CreateWindow1(self.IV1Value,self.IV2Value)])
        self.knapAdd.grid(row=0,column=0,padx=1)

        self.knapMin = LP.Button(self.knapFrame, text="Subtraktion", width=10,font=('Arial',28),command = lambda: [self.IV1ValueGet(),self.IV2ValueGet(),self.CreateWindow2(self.IV1Value,self.IV2Value)])
        self.knapMin.grid(row=0,column=1,padx=1)

        self.knapGan = LP.Button(self.knapFrame, text="Multiplikation", width=10,font=('Arial',28),command = lambda: [self.IV1ValueGet(),self.IV2ValueGet(), self.CreateWindow3(self.IV1Value,self.IV2Value)])
        self.knapGan.grid(row=0,column=2,padx=1)

        self.knapFrame.pack(padx=10,pady=10)

        self.IVFrame = LP.Frame(self.root)
        self.IVFrame.columnconfigure(0,weight=1)
        self.IVFrame.columnconfigure(1,weight=1)
        self.IVFrame.columnconfigure(2,weight=1)
        self.IVFrame.columnconfigure(3,weight=1)
        self.IVFrame.columnconfigure(4,weight=1)


        self.IVTal = LP.Label(self.IVFrame, text="Indsæt tal", font=('Arial',20))
        self.IVTal.grid(row=0,column=1,padx=1)

        self.IV1Label = LP.Label(self.IVFrame, text="Minimum:", font=('Arial',20))
        self.IV1Label.grid(row=1,column=0,padx=1)

        self.IV1 = LP.Entry(self.IVFrame,font=('Arial',20),width=8)
        self.IV1.grid(row=1,column=1,padx=1)


        self.IV2Label = LP.Label(self.IVFrame, text="Maksimum:", font=('Arial',20))
        self.IV2Label.grid(row=2,column=0,padx=1)

        self.IV2 = LP.Entry(self.IVFrame,font=('Arial',20),width=8)
        self.IV2.grid(row=2,column=1,padx=1)

        self.IVFrame.pack(padx=10,pady=20)

        self.HP_Knap = LP.Button(self.root, text="Hjælp", font=('Arial', 12), command=self.hjaelp)
        self.HP_Knap.pack(side=BOTTOM,pady=5)

        self.root.mainloop() 

    
    def hjaelp(self):
        HP = LP.Toplevel()
        HP.title('Hjælp')
        HP.geometry("800x400")

        def LukWindow():
            HP.destroy()

        Velkommen = LP.Label(HP,text="Velkommen til MatMA",font=('Arial', 38))
        Velkommen.pack(padx=5,pady=15)

        Tekst1 = LP.Label(HP,text="1. Indsæt venligst laveste og højste tal du vil regne med i indsæt tal boksen",font=('Arial', 20))
        Tekst1.pack(padx=5,pady=15)

        Tekst2 = LP.Label(HP,text="2. Vælg kategori man vil regne",font=('Arial', 20))
        Tekst2.pack(padx=5,pady=15)

        Tekst3 = LP.Label(HP,text="3. Indsæt dit gæt i feltet og tryk på tjek eller enter på tastaturet",font=('Arial', 20))
        Tekst3.pack(padx=5,pady=15)

        Tekst4 = LP.Label(HP,text="4. Tryk på næste for at få et nyt regnestykke",font=('Arial', 20))
        Tekst4.pack(padx=5,pady=15)


        TilbageKnap = LP.Button(HP, text="Tilbage til hovedmenu", font=('Arial', 12), command=LukWindow)
        TilbageKnap.pack(side=BOTTOM,pady=5)

    def IV1ValueGet(self):
        self.IV1Value = int(self.IV1.get())

    def IV2ValueGet(self):
        self.IV2Value = int(self.IV2.get())

    K1 = None
    F1 = None

    def CreateWindow1(self, IV1Value, IV2Value):
        Add_Window1 = LP.Toplevel()
        Add_Window1.title('Addition')
        Add_Window1.geometry("800x500")
        print(IV1Value)
        print(IV2Value)
        

        def RandomTal():
            if self.K1 is not None:
                self.K1.destroy()
            if self.F1 is not None:
                self.F1.destroy()
            
            random_number.set(random.randint(IV1Value, IV2Value))
            random_number2.set(random.randint(IV1Value, IV2Value))

            SP.config(text=f"{random_number.get()} + {random_number2.get()}")
            E1.delete(0, LP.END)

        random_number = LP.StringVar()
        random_number2 = LP.StringVar()

        SP = LP.Label(Add_Window1, text="", font=('Arial',80))
        SP.pack(padx=10,pady=35)

        E1 = LP.Entry(Add_Window1, font=('Arial',44), width=8)
        E1.pack(padx=10,pady=10)

        def C1(event=None):  
            user_svar = int(E1.get())
            print(user_svar)

            if self.K1 is not None:
                self.K1.destroy()
            if self.F1 is not None:
                self.F1.destroy()

            if user_svar == int(random_number.get()) + int(random_number2.get()):
                if self.F1 is not None:
                    self.F1.destroy()

                self.K1 = LP.Label(Add_Window1, text="Korrekt, godt gået", font=('Arial',40))
                self.K1.pack(padx=10,pady=10)

            else:
                self.F1 = LP.Label(Add_Window1, text=f"Forkert svar, det rigtige svar er {int(random_number.get()) + int(random_number2.get())}", font=('Arial',40))
                self.F1.pack(padx=10,pady=10)

        B1 = LP.Button(Add_Window1, text="Tjek", font=('Arial', 28), command=C1)
        B1.pack()
        
        B2 = LP.Button(Add_Window1, text="Næste", font=('Arial', 28), command=RandomTal)
        B2.pack()

        E1.bind("<Return>", C1)

        def LukWindow():
            Add_Window1.destroy()

        TilbageKnap = LP.Button(Add_Window1, text="Tilbage til hovedmenu", font=('Arial', 12), command=LukWindow)
        TilbageKnap.pack(side=BOTTOM,pady=5)

        RandomTal()
    
    def CreateWindow2(self,IV1Value,IV2Value):
        Add_Window2 = LP.Toplevel()
        Add_Window2.title('Subtraktion')
        Add_Window2.geometry("800x500")

        print(IV1Value)
        print(IV2Value)

        def RandomTal():
            if self.K1 is not None:
                self.K1.destroy()
            if self.F1 is not None:
                self.F1.destroy()
            
            random_number.set(random.randint(IV1Value, IV2Value))
            random_number2.set(random.randint(IV1Value, IV2Value))

            SP.config(text=f"{random_number.get()} - {random_number2.get()}")
            E1.delete(0, LP.END)

        random_number = LP.StringVar()
        random_number2 = LP.StringVar()

        SP = LP.Label(Add_Window2, text="", font=('Arial',80))
        SP.pack(padx=10,pady=35)

        E1 = LP.Entry(Add_Window2, font=('Arial',44), width=8)
        E1.pack(padx=10,pady=10)

        def C1(event=None):  
            user_svar = int(E1.get())
            print(user_svar)

            if self.K1 is not None:
                self.K1.destroy()
            if self.F1 is not None:
                self.F1.destroy()

            if user_svar == int(random_number.get()) - int(random_number2.get()):
                if self.F1 is not None:
                    self.F1.destroy()

                self.K1 = LP.Label(Add_Window2, text="Korrekt, godt gået", font=('Arial',40))
                self.K1.pack(padx=10,pady=10)

            else:
                self.F1 = LP.Label(Add_Window2, text=f"Forkert svar, det rigtige svar er {int(random_number.get()) - int(random_number2.get())}", font=('Arial',40))
                self.F1.pack(padx=10,pady=10)

        B1 = LP.Button(Add_Window2, text="Tjek", font=('Arial', 28), command=C1)
        B1.pack()
        
        B2 = LP.Button(Add_Window2, text="Næste", font=('Arial', 28), command=RandomTal)
        B2.pack()

        E1.bind("<Return>", C1)

        def LukWindow():
            Add_Window2.destroy()

        TilbageKnap = LP.Button(Add_Window2, text="Tilbage til hovedmenu", font=('Arial', 12), command=LukWindow)
        TilbageKnap.pack(side=BOTTOM,pady=5)

        RandomTal()

    def CreateWindow3(self, IV1Value, IV2Value):
        Add_Window3 = LP.Toplevel()
        Add_Window3.title('Multiplikation')
        Add_Window3.geometry("800x500")

        print(IV1Value)
        print(IV2Value)

        def RandomTal():
            if self.K1 is not None:
                self.K1.destroy()
            if self.F1 is not None:
                self.F1.destroy()
            
            random_number.set(random.randint(IV1Value, IV2Value))
            random_number2.set(random.randint(IV1Value, IV2Value))

            SP.config(text=f"{random_number.get()} * {random_number2.get()}")
            E1.delete(0, LP.END)

        random_number = LP.StringVar()
        random_number2 = LP.StringVar()

        SP = LP.Label(Add_Window3, text="", font=('Arial',80))
        SP.pack(padx=10,pady=35)

        E1 = LP.Entry(Add_Window3, font=('Arial',44), width=8)
        E1.pack(padx=10,pady=10)

        def C1(event=None):  
            user_svar = int(E1.get())
            print(user_svar)

            if self.K1 is not None:
                self.K1.destroy()
            if self.F1 is not None:
                self.F1.destroy()

            if user_svar == int(random_number.get()) * int(random_number2.get()):
                if self.F1 is not None:
                    self.F1.destroy()

                self.K1 = LP.Label(Add_Window3, text="Korrekt, godt gået", font=('Arial',40))
                self.K1.pack(padx=10,pady=10)

            else:
                self.F1 = LP.Label(Add_Window3, text=f"Forkert svar, det rigtige svar er {int(random_number.get()) * int(random_number2.get())}", font=('Arial',40))
                self.F1.pack(padx=10,pady=10)

        B1 = LP.Button(Add_Window3, text="Tjek", font=('Arial', 28), command=C1)
        B1.pack()
        
        B2 = LP.Button(Add_Window3, text="Næste", font=('Arial', 28), command=RandomTal)
        B2.pack()

        E1.bind("<Return>", C1)

        def LukWindow():
            Add_Window3.destroy()

        TilbageKnap = LP.Button(Add_Window3, text="Tilbage til hovedmenu", font=('Arial', 12), command=LukWindow)
        TilbageKnap.pack(side=BOTTOM,pady=5)

        RandomTal()

LPapp()


