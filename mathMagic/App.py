import tkinter as tk

def afficher_message():
    label.config(text="Bonjour, vous avez cliqué sur le bouton !")

# Création de la fenêtre
fenetre = tk.Tk()
fenetre.title("Ma première application")

# Création d'un bouton
bouton = tk.Button(fenetre, text="Cliquez-moi !", command=afficher_message)
bouton.pack(pady=10)

# Création d'une étiquette
label = tk.Label(fenetre, text="")
label.pack()

# Boucle principale de l'application
fenetre.mainloop()
