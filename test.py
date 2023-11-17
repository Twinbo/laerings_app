#Import the required Libraries
from tkinter import *
from tkinter import ttk

#Create an instance of Tkinter frame
win= Tk()
import random

#Set the geometry of Tkinter frame
win.geometry("750x250")

def display_text():
   global entry
   string= entry.get()
   label.configure(text=string)

#Initialize a Label to display the User Input
label=Label(win, text="", font=("Courier 22 bold"))
label.pack()

#Create an Entry widget to accept User Input
entry= Entry(win, width= 40)
entry.focus_set()
entry.pack()

#Create a Button to validate Entry Widget
ttk.Button(win, text= "Okay",width= 20, command= display_text).pack(pady=20)

win.mainloop()

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


#def display_p():
 #       global entry
#      inputP = entry
 #       labelPPP.configure(text=inputP)
  #  
   # labelPPP=LP.Label(Add_Window1,text="",font=('Arial',24 )).pack(padx=10,pady=10)
    
    #entry = LP.Entry(Add_Window1, width=40).pack(padx=10,pady=10)
    #entry.focus_set()
   
  #  LP.Button(Add_Window1, text="Godkend", width=20, command= display_p()).pack(pady=20)


   # LP.Label(Add_Window1,text="Plus regnestykker", font=('Arial',24 )).pack(padx=10,pady=26)




def CreateWindow1():
    Add_Window1 = LP.Toplevel()
    Add_Window1.title('Addition')
    Add_Window1.geometry("800x500")

    def RT():
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
            K1 = LP.Label(Add_Window1, text="Korrekt, godt gået", font=('Arial',40))
            K1.pack(padx=10,pady=10)
            #print("Det er rigtigt, Godt gået1")

        else:
            F1 = LP.Label(Add_Window1, text=f"Forkert svar, det rigtige svar er {int(random_number.get()) + int(random_number2.get())}", font=('Arial',40))
            F1.pack(padx=10,pady=10)
            #print("Svaret er forkert, det rigtige svar var", int(random_number.get()) + int(random_number2.get()))

    B1 = LP.Button(Add_Window1, text="Tjek", font=('Arial', 20), command=C1).pack(padx=10,pady=10)
    B2 = LP.Button(Add_Window1, text="Næste", font=('Arial', 20),command=RT).pack(padx=10,pady=10)
    
    RT()