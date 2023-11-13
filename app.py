#laering program 

import tkinter as LP

class   MyGui:
#class   LPapp:


    def __init__(self):

        self.root = LP.Tk()
        self.root.geometry("800x500")


        self.root.geometry("800x500")
        self.root.title("MatLæring")

        self.label1 = LP.Label(self.root, text="Lorte Unger", font=('Arial',44))
        self.label1.pack(padx=10,pady=60)

        self.label = LP.Label(self.root, text="Vælg kategori", font=('Arial',24))
        self.label.pack(padx=10,pady=10)

        #textbox = LP.Text(root, height=1, width=30,font=('Arial',16))
        #textbox.pack(pady=10)
        self.textbox = LP.Text(self.root, height=1, width=30,font=('Arial',16))
        self.textbox.pack(pady=10)

        self.kanpFrame = LP.Frame(self.root)
        self.kanpFrame.columnconfigure(0,weight=1)
        self.kanpFrame.columnconfigure(1,weight=1)
        self.kanpFrame.columnconfigure(2,weight=1)

        self.knapAdd = LP.Button(self.root.kanpFrame, text="Addition", width=10,font=('Arial',28))
        self.knapAdd.grid(row=0,column=0,padx=1)

        self.knapMin = LP.Button(self.root.kanpFrame, text="Subtraktion", width=10,font=('Arial',28))
        self.knapMin.grid(row=0,column=1,padx=1)

        self.knapGan = LP.Button(self.root.kanpFrame, text="Multiplikation", width=10,font=('Arial',28))
        self.knapAdd = LP.Button(self.kanpFrame, text="Addition", width=10,font=('Arial',28))
        self.knapAdd.grid(row=0,column=0,padx=1)

        self.knapMin = LP.Button(self.kanpFrame, text="Subtraktion", width=10,font=('Arial',28))
        self.knapMin.grid(row=0,column=1,padx=1)

        self.knapGan = LP.Button(self.kanpFrame, text="Multiplikation", width=10,font=('Arial',28))
        self.knapGan.grid(row=0,column=2,padx=1)

        self.kanpFrame.pack(padx=10,pady=20)

        self.root.mainloop() 

#def lukProgram(self):
    #if 


LPapp()
