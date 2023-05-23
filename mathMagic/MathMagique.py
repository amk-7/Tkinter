from pylab import linspace, cos, sin, pi
from tkinter.messagebox import showerror, showinfo
import tkinter as tk
import numpy as np

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Math magique')
        self.geometry("1080x720")
        self.minsize(1150, 765)	
        self.maxsize(1150, 765)	
        self.bg_color = "#E77100"
        self.config(background = self.bg_color)
        self.heightWiget = 700
        self.frameGraphique = tk.Frame(master=self, height=self.heightWiget , width=700, bg="#fff")
        self.frameGraphique.place(x=10, y=10)
        
        self.frameMenu = tk.Frame(master=self, height=self.heightWiget , width=300, bg="#fff")
        self.frameMenu.place(x=725, y=10)
        self.setMenu()
        
        # animation principlale
        self.sinAnimationValue = 0.5

        # Default graphique
        self.defaultGraphique()
        

    
    def setMenu(self):
        
        title = tk.Label(master=self.frameMenu, text="Menu", font=("Courrier", 20), bg="white", fg="#E77100")
        title.pack()

        #Use case Multiplication
        frameMultiplication = tk.Frame(master=self.frameMenu, bg="white")
        frameMultiplication.pack()
        multiplication = tk.Label(master=frameMultiplication, text="Tables de multiplications", font=("Courrier", 15), bg="white", fg="#E77100")
        multiplication.pack()
        
        table = tk.Label(master=frameMultiplication, text="Table", font=("Courrier", 10), bg="white", fg="#E77100")
        table.pack()
        self.entryTable = tk.Entry(master=frameMultiplication)
        self.entryTable.pack()

        modulo = tk.Label(master=frameMultiplication, text="Modulo", font=("Courrier", 10), bg="white", fg="#E77100")
        modulo.pack()
        self.entryModulo = tk.Entry(master=frameMultiplication)
        self.entryModulo.pack()

        nbImage = tk.Label(master=frameMultiplication, text="Nombre d'images", font=("Courrier", 10), bg="white", fg="#E77100")
        nbImage.pack()
        self.entryNbImage = tk.Entry(master=frameMultiplication)
        self.entryNbImage.pack()

        pas = tk.Label(master=frameMultiplication, text="Pas", font=("Courrier", 10), bg="white", fg="#E77100")
        pas.pack()
        self.entryPas = tk.Entry(master=frameMultiplication, font=("courrier", 10), fg="black")
        self.entryPas.pack()


        self.generateGrapheTable = tk.Button(frameMultiplication, text="Simuler", font=("Courrier", 20), bg="white", fg=self.bg_color, command = self.multiplieTable)
        self.generateGrapheTable.pack()

        #use case fonction.

        frameFonction = tk.Frame(master=self.frameMenu, bg="white")
        frameFonction.pack()
        fonction = tk.Label(master=frameFonction, text="\nEquations quadratique : F(x)=ax²+bx+c\n", font=("Courrier", 15), bg="white", fg="#E77100")
        fonction.pack()
        
        alabel = tk.Label(master=frameFonction, text="a", font=("Courrier", 10), bg="white", fg="#E77100")
        alabel.pack()
        self.entryA = tk.Entry(master=frameFonction)
        self.entryA.pack()

        
        blabel = tk.Label(master=frameFonction, text="b", font=("Courrier", 10), bg="white", fg="#E77100")
        blabel.pack()
        self.entryB = tk.Entry(master=frameFonction)
        self.entryB.pack()

        clabel = tk.Label(master=frameFonction, text="c", font=("Courrier", 10), bg="white", fg="#E77100")
        clabel.pack()
        self.entryC = tk.Entry(master=frameFonction)
        self.entryC.pack()


        self.generateGrapheFunction = tk.Button(frameFonction, text="Simuler", font=("Courrier", 20), bg="white", fg=self.bg_color, command = self.drawFonction)
        self.generateGrapheFunction.pack()

        sinlabel = tk.Label(master=frameFonction, text="\nSinusoide", font=("Courrier", 20), bg="white", fg="#E77100")
        sinlabel.pack()

        self.generateGrapheSin = tk.Button(frameFonction, text="Activer", font=("Courrier", 20), bg="white", fg=self.bg_color, command = self.sinusoidGraphique)
        self.generateGrapheSin.pack()

        self.curseur = tk.Scale(master=frameFonction, orient = "horizontal", command=self.changeSinAnimateValue, from_=0, to=100, bg="white", fg="#E77100", width=15, length=200)
        self.curseur.pack()


    def defaultGraphique(self):
        # create a figure w,h 77        
        self.figure = Figure(figsize=(7, 7), dpi=100)

        # create FigureCanvasTkAgg object
        self.figure_canvas = FigureCanvasTkAgg(self.figure, self.frameGraphique)

        # create the toolbar
        self.toolbar = NavigationToolbar2Tk(self.figure_canvas, self.frameGraphique)
        self.toolbar.update() 
        
        # Defind axes
        self.axes = self.figure.add_subplot()

        # show the canvas
        self.figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.sinusoidGraphique()

    def changeSinAnimateValue(self, x):
          self.sinAnimationValue = self.sinAnimationValue=float(x)/100
          #print(self.sinAnimationValue)
        
    def sinusoidGraphique(self):
        self.axes.clear()

        x = linspace(0, 10*np.pi, 100)
        y = np.sin(x)  
        line, = self.axes.plot(x, y, 'k.')

        while True:
            for phase in x:
                line.set_ydata(np.sin(self.sinAnimationValue * x + phase))
                self.updating()


    def updating(self):
        self.figure_canvas.draw()
        self.figure_canvas.flush_events()
        #

    def desableButton(self):
        self.generateGrapheTable['state'] = tk.DISABLED
        self.generateGrapheFunction['state'] = tk.DISABLED
        self.generateGrapheSin['state'] = tk.DISABLED

    def enableButton(self):
        self.generateGrapheTable['state'] = tk.NORMAL
        self.generateGrapheFunction['state'] = tk.NORMAL
        self.generateGrapheSin['state'] = tk.NORMAL


    def drawFonction(self):
        self.update()
        self.axes.clear()

        a = self.entryA.get()
        b = self.entryB.get()
        c = self.entryC.get()

        try:
            a= float(a)
        except ValueError:
            showerror("'a' incorrect", "la valeur de a doit être positif")
            return
        
        try:
            b= float(b)
        except ValueError:
            showerror("'b' incorrect", "la valeur de b doit être positif")
            return
        
        try:
            c= float(c)
        except ValueError:
            showerror("'c' incorrect", "la valeur de c doit être positif")
            return

        y=[a*i**2+b*i+c for i in range(-100, 100)]

        self.axes.plot(y,'k')

        self.updating()


    def drawTable(self, multiplicateur, modulo):

        self.axes.clear()
        r=1
    
        # le cercle
        alpha=linspace(0,2*pi,200)
        x=r*cos(alpha)
        y=r*sin(alpha)
        self.axes.plot(x, y, "k")
        #self.updating()

        #le modulo
        taille=modulo+1
        alpha=linspace(0,2*pi,taille)
        x=r*cos(alpha)
        y=r*sin(alpha)
        self.axes.plot(y,x,'k.')
        
        #self.updating()

        #la figure en question
        unelignex=[]
        uneligney=[]

        self.axes.set_title("Table de "+str(multiplicateur))
        
        for nombre in range(1,modulo+1):
            
            resultat = multiplicateur*nombre
            
            # lorsque le resultat est un réele 
            
            resultat_entier = int(resultat)
            resultat_virgule =resultat-resultat_entier
            resultat=resultat_entier
            unelignex.append(x[nombre])
            uneligney.append(y[nombre])
            
            if  resultat <=10:
                unelignex.append(x[resultat]+resultat_virgule)
                uneligney.append(y[resultat]+resultat_virgule)
            else:
                quotient=resultat//modulo
                equilibre=(quotient*modulo)
                resultat-=equilibre
                unelignex.append(x[resultat]+resultat_virgule)
                uneligney.append(y[resultat]+resultat_virgule)
                
            self.axes.plot(uneligney,unelignex,'k')

            unelignex=[]
            uneligney=[]

            self.updating()
        


        
        
    def multiplieTable(self):
        
        table = self.entryTable.get()
        modulo = self.entryModulo.get()
        tours = self.entryNbImage.get()
        pas = self.entryPas.get()

        
        if not(table.isdecimal()):
            showerror("Table invalide", "La table doit être positif")
            return 

        if not(modulo.isdecimal()) :
            showerror("Modulo Invalide", "Le modulo doit être positif.")
            return
        
        if not(tours.isdecimal()):
            showerror("Nombre invalide", "Le nombre d'image doit être positif")
            return
        
        
        try:
            pas=float(pas)
        except ValueError:
            showerror("Pas Invalide", "Le pas doit être positif ou nule")
            return

        self.desableButton()

        table=float(table)
        modulo=int(modulo)
        tours=int(tours)
        pas = float(pas)

        if modulo >= 10 and table > 0:
            for i in range(tours):
                self.drawTable(table, modulo)
                table += pas
        else:
            showerror("Erreur", "Le modulo est un nombre >= 10 et la table un nombre > 0")

        self.enableButton()
            
       

        

if __name__ == '__main__':
    app = App()
    app.mainloop()