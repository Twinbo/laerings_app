#Importer alt fra tkinter
from tkinter import *
from abc import ABC, abstractmethod 

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class SetBlackBackground(Command):
    def init(self):
        super()



    def execute(self):
        root.configure(background='green')


dui = SetBlackBackground()
#Lav et tkinter vindue
root = Tk()
 
#Åben vinduet
root.geometry('100x100') 

#Lav en knap
btnBlack = Button(root, text = 'Knap baggrund !', bd = '5',
                          command = dui.execute) 
 
#Sæt positionen af knap på vindue
btnBlack.pack(side = 'top')
 
root.mainloop()

#https://github.com/Twinbo/laerings_app.git

#HOW TO SAVE TO CLOUD AFTER CHANGES TO CODE

#git init 
#git add -A
#git status 
#git commit -m 'navn på commit'
#git push -u origin master