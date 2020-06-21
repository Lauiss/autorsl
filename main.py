from tkinter import *

#Crée la fenêtre + Paramètres
window = Tk()
window.title("Farmer Raid")
window.minsize(700, 800)
window.maxsize(700, 800)
window.iconbitmap("Kael.ico")
window.config(bg="black")

#frames

frame1 = Frame(window,bg="black", width=700, height=200)
frame2line = Frame(window,bg="white", width=700, height=5)
frame3 = Frame(window, bg="black", width=700, height=390)
frame4line = Frame(window, bg="yellow", width=700, height=5)
frame5 = Frame(window, bg="black", width=700, height=200)

#canvas
height = 150
width = 150
kael = PhotoImage(file="Kael.png").zoom(4).subsample(32)
canvaskael = Canvas(frame1, width=width, height=height, bg='black', bd=0, highlightthickness=0)
canvaskael.create_image(width/2, height/2, image=kael)
canvaskael.pack(side=LEFT)

height = 150
width = 150
galek = PhotoImage(file="Galek.png").zoom(8).subsample(32)
canvasgalek = Canvas(frame1, width=width, height=height, bg='black', bd=0, highlightthickness=0)
canvasgalek.create_image(width/2, height/2, image=galek)
canvasgalek.pack(side=RIGHT)

height = 150
width = 150
horde = PhotoImage(file="horde.png").zoom(13).subsample(32)
canvashorde = Canvas(frame3, width=width, height=height, bg='black', bd=0, highlightthickness=0)
canvashorde.create_image(width/2, height/2, image=horde)
canvashorde.pack(side=LEFT)

height = 150
width = 150
hautselfs = PhotoImage(file="hautselfs.png").zoom(13).subsample(32)
canvaself = Canvas(frame3, width=width, height=height, bg='black', bd=0, highlightthickness=0)
canvaself.create_image(width/2, height/2, image=hautselfs)
canvaself.pack(side=RIGHT)

# Labels
label_title = Label(frame1, text="Farmer Raid", font=("Impact", 50), bg='black', fg='white')
label_title.pack(pady=30, padx=32)

label_infotitle = Label(frame5, text="Informations :", font=("Impact",15), bg='black', fg='yellow')
label_infotitle.pack(pady=10)

label_info = Label(frame5, text="- Entrez un délai (nombre entier) pour l'auto-clicker, il cliquera toutes les (délai) secondes\n\n"
                   "- Appuyez sur le bouton coordonnées et cliquez là où l'auto-clicker devra cliquer. \n\n"
                   "- Appuyez sur commencer pour lancer l'auto-clicker.\n\n"
                   "- Appuyez sur la touche 'échap' pour arrêter l'auto-clicker.", font=("Arial",12), bg='black',
                   fg='yellow')
label_info.pack(pady=20)

# Button

button_coor = Button(frame3, text="Coordonnées", font=("Arial",20), width=20, height=1,
                     bd=5, highlightthickness=5, activebackground='#A7A7A7')

button_validate = Button(frame3, text="Valider l'intervalle", font=("Arial",20), width=20, height=1,
                         bd=5, highlightthickness=5, activebackground='#A7A7A7')

button_commencer = Button(frame3, text="Commencer", font=("Arial", 20), width=20, height=1,
                          bd=5, highlightthickness=5, activebackground='#A7A7A7')


#Entrée

inter_sec = Entry(frame3, font=("Arial",23), bd=3, highlightthickness=3, justify=CENTER)
inter_sec.pack(pady=20)


# button pack
button_validate.pack(pady=15)
button_coor.pack(pady=15)
button_commencer.pack(pady=15)

#Personnalisation
def persomode(background, buttoncolor, activebutton, activefont):
    window.config(bg=background)
    button_coor.config(bg=buttoncolor)
    button_coor.config(activebackground=activebutton)
    button_coor.config(activeforeground=activefont)
    button_validate.config(bg=buttoncolor)
    button_validate.config(activebackground=activebutton)
    button_validate.config(activeforeground=activefont)
    button_commencer.config(bg=buttoncolor)
    button_commencer.config(activebackground=activebutton)
    button_commencer.config(activeforeground=activefont)
    frame1.config(bg=background)
    frame3.config(bg=background)
    frame5.config(bg=background)
    canvaskael.config(bg=background)
    canvasgalek.config(bg=background)
    canvashorde.config(bg=background)
    canvaself.config(bg=background)
    label_title.config(bg=background)
    label_infotitle.config(bg=background)
    label_info.config(bg=background)


def mode_jour():
    persomode(background="#6C1FB8", buttoncolor="#F38539", activebutton="#AB4F10",
                                 activefont="#A4A4A4")

def mode_nuit():
    persomode(background="#060830", buttoncolor="#581CA1", activebutton="#310961",
                                 activefont="#A4A4A4")

def mode_marin():
    persomode(background= "#0530C2",buttoncolor= "#4793FA",activebutton= "#0849A2",
                                 activefont= "#A4A4A4")

def mode_girly():
    persomode(background= "#670D6A", buttoncolor= "#F460F7", activebutton= "#971B9A",
                                 activefont= "#A4A4A4")

def mode_defaut():
    persomode(background="black", buttoncolor="white", activebutton="#A7A7A7", activefont="black")


#Menu
menu_bar = Menu(window)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Actions", menu=file_menu)
window.config(menu=menu_bar)


perso_menu = Menu(menu_bar, tearoff=0)
perso_menu.add_command(label="Defaut", command=lambda:mode_defaut())
perso_menu.add_command(label="Mode Jour", command=lambda:mode_jour())
perso_menu.add_command(label="Mode Nuit", command=lambda:mode_nuit())
perso_menu.add_command(label="Mode Marin", command=lambda:mode_marin())
perso_menu.add_command(label="Mode Girly", command=lambda:mode_girly())
menu_bar.add_cascade(label="Personnalisation", menu=perso_menu)

#pack des frames
frame1.pack()
frame2line.pack()
frame3.pack()
frame4line.pack()
frame5.pack()

# afficher la fenêtre
window.mainloop()