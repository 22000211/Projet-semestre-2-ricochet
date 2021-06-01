import tkinter as tk
import tkinter.font as tkFont
import os
import random
from tkinter.filedialog import *
from tkinter.messagebox import *
from PIL import Image #pour le score
from PIL import ImageTk #pour le score


#Romane GENSE
def selection(event):
    #fonction qui séléctionne l'objet à déplacer grâce à un clic
    global robot
    x, y = event.x, event.y
    robot = event.widget.find_closest(x, y)
    if (robot==(178,)):   #Perrine ILARY
        Nouvelle_Partie() #ID=178 centre du Canvas et ensuite 364
    event.widget.coords(robot[0]) 

#Romane GENSE & Perrine ILARY & Sabah KEBLI
def droite(event):
    global robot,car,robot_bleu
    coord =canvas.coords(robot_bleu)
    #permet de déplacer l'objet séléctionné à droite avec la flèche correspondante du clavier
    if (robot==(184,) and (coord[0]<15*37.5)): #si touche OK et on sort pas de l'écran
        canvas.move(robot,taillex,0)
        #racine.after(20,droite, event) 
        mouvement.append('droite')
        car += 1    #P. ILARY
        affich_Score (car)  #P. ILARY
        xxx[0] = xxx[0] + taillex  #Sabah
        xxx[2] = xxx[2] + taillex
        ess()
    elif (robot==(182,)) or (robot==(183,)) or (robot==(185,)):
        canvas.move(robot,taillex,0)
        #racine.after(20,droite, event)
        mouvement.append('droite')
        car += 1    
        affich_Score (car)
 
#Romane GENSE & Perrine ILARY & Sabah KEBLI
def gauche(event):
    global robot, car
    coord =canvas.coords(robot_bleu)
    #permet de déplacer l'objet séléctionné à gauche avec la flèche correspondante du clavier
    if (robot==(184,) and (coord[0]>=37.5)): #si touche OK et on sort pas de l'écran
        canvas.move(robot,-taillex,0)
        #racine.after(20,gauche, event) 
        mouvement.append('gauche')
        car += 1    #P. ILARY
        affich_Score (car)  #P. ILARY
        xxx[0] = xxx[0] - taillex   #Sabah
        xxx[2] = xxx[2] - taillex
        ess()
    elif (robot==(182,)) or (robot==(183,)) or (robot==(185,)):
        canvas.move(robot,-taillex,0)
        #racine.after(20,gauche, event) 
        mouvement.append('droite')
        car += 1    
        affich_Score (car)

#Romane GENSE & Perrine ILARY & Sabah KEBLI
def haut(event):
    global robot, car
    coord =canvas.coords(robot_bleu)
    #permet de déplacer l'objet séléctionné à gauche avec la flèche correspondante du clavier
    if (robot==(184,) and (coord[1]>=37.5)): #si touche OK et on sort pas de l'écran
        canvas.move(robot,0,-tailley)
        #racine.after(20,haut, event) 
        mouvement.append('haut')
        car += 1    #P. ILARY
        affich_Score (car)  #P. ILARY
        xxx[1] = xxx[1] - tailley
        xxx[3] = xxx[3] - tailley
        ess()
    elif (robot==(182,)) or (robot==(183,)) or (robot==(185,)):
        canvas.move(robot,0,-tailley)
        #racine.after(20,haut, event) 
        mouvement.append('droite')
        car += 1    
        affich_Score (car)

#Romane GENSE & Perrine ILARY & Sabah KEBLI & Romane DONAT
def bas(event):
    global robot, car
    coord =canvas.coords(robot_bleu)    
    #permet de déplacer l'objet séléctionné à gauche avec la flèche correspondante du clavier
    if (robot==(184,) and (coord[1]<15*37.5)): #si touche OK et on sort pas de l'écran
        canvas.move(robot,0,tailley)
        #racine.after(20,bas, event) 
        mouvement.append('bas')
        car += 1    #score+1
        affich_Score (car)  
        xxx[1] = xxx[1] + tailley
        xxx[3] = xxx[3] + tailley
        ess()
    elif (robot==(182,)) or (robot==(183,)) or (robot==(185,)):
        canvas.move(robot,0,tailley)
        #racine.after(20,bas, event)
        mouvement.append('droite')
        car += 1    
        affich_Score (car)


racine = tk.Tk()


# Initialisation des constantes & variables

#Perrine ILARY
# Chargement de la police de caractères
image_Font = Image.open(os.path.dirname(os.path.abspath(__file__))+"/Font4.png")
Nom_saisi = ''
Dx_font = 30    #largeur de la police (image)
Dy_font = 30    #hauteur de la police (image)

#Romane GENSE
mouvement=[]
xb0, yb0 = 262.5, 487.5
xg0, yg0 = 562.5, 75
xy0, yy0 = 150, 262.5
xr0, yr0 = 450, 375
xc0, yc0 = 187.5, 75
taillex, tailley = 37.5, 37.5
 

#Romane GENSE
trait_haut=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],\
    [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0],\
        [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]

trait_bas=[[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0],\
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],\
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

trait_droite=[[0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],\
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],\
        [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],\
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],\
                [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1]]

trait_gauche=[[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],\
    [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],\
        [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],[1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],\
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]]



#Fonction d'initialisation de début de partie
#Romane GENSE
def init():
    global xb, xy, xg, xr, xc, yb, yy, yg, yr, yc, car, list_posx, list_posy, arrivee_pos,xxx
    xb, yb = xb0, yb0
    xg, yg = xg0, yg0
    xy, yy = xy0, yy0
    xr, yr = xr0, yr0
    xc, yc = xc0, yc0
    car =0          #nombre de déplacements
    list_posx=[0,0,0,0,0] #initialiser à 0
    list_posy=[0,0,0,0,0]
    arrivee_pos=[0,0,0,0] #coordonnées de l'arrivée définit plus loin
    xxx=[0,0,0,0]


#On dessine le terrain
#Romane GENSE
def dessiner_terrain():
    a, u = 0, 0
    while a != 16 :
        canvas.create_line(37.5+u,0, 37.5+u,600)
        canvas.create_line(0,37.5+u, 600,37.5+u)
        canvas.create_line(3,0+u,3,37.5+u, fill="black",width=3)
        canvas.create_line(0+u,3,37.5+u,3, fill="black",width=3)
        u += 37.5
        a+=1

    for i in range(0, 16):
        for j in range(0, 16):
            if trait_haut[i][j]==1 :
                canvas.create_line((37.5*j),(37.5*i),(37.5*(j+1)),(37.5*i), fill="black",width=4)
            if trait_bas[i][j]==1 :
                canvas.create_line((37.5*j),(37.5*(i+1)),(37.5*(j+1)),(37.5*(i+1)), fill="black",width=4)
            if trait_droite[i][j]==1:
                canvas.create_line((37.5*(j+1)),(37.5*i),(37.5*(j+1)),(37.5*(i+1)), fill="black",width=4)
            if trait_gauche[i][j]==1:
                canvas.create_line((37.5*j),(37.5*i),(37.5*j),(37.5*(i+1)), fill="black",width=4)
    #Dessine la zone de réinitialisation de la partie (au centre du canvas)
    replay=canvas.create_rectangle(337.5,337.5,262.5,262.5, fill='black', tags='rect')
    canvas.addtag_withtag("rect",replay)
    canvas.create_oval(330.5,330.5,269.5,269.5,outline='white')
    canvas.create_line(332.1, 298, 332.5, 299, arrow="last", fill="white")
    canvas.create_line(268.1, 301, 268.5, 302, arrow="first", fill="white")

def Pos_aleatoire():
    global list_posx
    global list_posy
    pos=0 #Quel robot? bleu=0 à zone d'arrivée=4
    valid=0 #permet de savoir si les coordonnées ne sont pas déjà affectées 
    alea_x=random.randint(0,15)
    alea_y=random.randint(0,15)
    list_posx[pos]=alea_x
    list_posy[pos]=alea_y
    pos=1
    while pos<5:
        alea_x=random.randint(0,15)
        alea_y=random.randint(0,15)
        for i in range(pos):
            if (not((alea_x==list_posx[i]) and (alea_y==list_posy[i])) and (not((alea_x==7)and(alea_y==7)) and not((alea_x==8)and(alea_y==7)) and not((alea_x==7)and(alea_y==8)) and not((alea_x==8)and(alea_y==8)))):
                valid+=1 #Valide si pas déjà pris par un robot (ou arrivée) et pas la zone centrale noire
        if valid==pos:
            list_posx[pos]=alea_x
            list_posy[pos]=alea_y
            valid=0
            pos+=1

#Romane GENSE
def creer_robots():
    #création et placement des robots et de la case de fin
    global robot_bleu, robot_jaune, robot_rouge, robot_vert, arrivee, arrivee_pos,xxx
#   canvas.create_rectangle(xc, yc, xc + taillex - 2, yc + tailley - 2, fill="blue")
    pos=0
    robot_jaune=canvas.create_oval(list_posx[pos]*taillex,list_posy[pos]*tailley,(list_posx[pos]+1)*taillex,(list_posy[pos]+1)*tailley, fill="yellow")
    pos=1
    robot_vert=canvas.create_oval(list_posx[pos]*taillex,list_posy[pos]*tailley,(list_posx[pos]+1)*taillex,(list_posy[pos]+1)*tailley, fill="green")
    pos=2
    robot_bleu=canvas.create_oval(list_posx[pos]*taillex,list_posy[pos]*tailley,(list_posx[pos]+1)*taillex,(list_posy[pos]+1)*tailley, fill="blue")
    xxx = [list_posx[pos]*taillex,list_posy[pos]*tailley,(list_posx[pos]+1)*taillex,(list_posy[pos]+1)*tailley]
    pos=3
    robot_rouge=canvas.create_oval(list_posx[pos]*taillex,list_posy[pos]*tailley,(list_posx[pos]-1)*taillex,(list_posy[pos]-1)*tailley, fill="red")
    pos=4
    arrivee=canvas.create_rectangle(list_posx[pos]*taillex,list_posy[pos]*tailley,(list_posx[pos]+1)*taillex-1,(list_posy[pos]+1)*tailley-1, fill="blue")  #Affiche la zone d'arrivée bleu
    arrivee_pos=[list_posx[pos]*taillex,list_posy[pos]*tailley,(list_posx[pos]+1)*taillex,(list_posy[pos]+1)*tailley]

#Romane GENSE & Perrine ILARY
def placer_robots():
    #création et placement des robots et de la case de fin
    global robot_bleu, robot_jaune, robot_rouge, robot_vert, canvas, arrivee, arrivee_pos,xxx

    pos=0
    canvas.coords(robot_jaune, list_posx[pos]*taillex,list_posy[pos]*tailley,(list_posx[pos]+1)*taillex,(list_posy[pos]+1)*tailley)
    pos=1
    canvas.coords(robot_vert, list_posx[pos]*taillex,list_posy[pos]*tailley,(list_posx[pos]+1)*taillex,(list_posy[pos]+1)*tailley)
    pos=2
    canvas.coords(robot_bleu, list_posx[pos]*taillex,list_posy[pos]*tailley,(list_posx[pos]+1)*taillex,(list_posy[pos]+1)*tailley)
    xxx = [list_posx[pos]*taillex,list_posy[pos]*tailley,(list_posx[pos]+1)*taillex,(list_posy[pos]+1)*tailley]
    pos=3
    canvas.coords(robot_rouge, list_posx[pos]*taillex,list_posy[pos]*tailley,(list_posx[pos]+1)*taillex,(list_posy[pos]+1)*tailley)
    pos=4
    canvas.coords(arrivee, list_posx[pos]*taillex,list_posy[pos]*tailley,(list_posx[pos]+1)*taillex,(list_posy[pos]+1)*tailley)
    arrivee_pos=[list_posx[pos]*taillex,list_posy[pos]*tailley,(list_posx[pos]+1)*taillex,(list_posy[pos]+1)*tailley]

#Sabah KEBLI & Perrine ILARY
def ess():
    global xxx, arrivee_pos,car
    global nom
    global fin
    global Nom_saisi
 
    print("xxx= ",xxx)
    print("arrivee_pos= ",arrivee_pos)
    if xxx == arrivee_pos:
        fin = tk.Toplevel(racine)
        tk.Label(fin, text="VOUS AVEZ REUSSI LE JEU",bg = "red").grid(row=0,column=0)
        print("VOUS AVEZ REUSSI LE JEU")
        tk.Label(fin, text="Votre nom").grid(row=1,column=0)
        nom = tk.Entry(fin)
        nom.grid(row=1, column=1)
        nom.bind('<Return>', (lambda event: saisie(car)))
        btn=tk.Button(fin,text="Quitter",command=fin.destroy)
        btn.grid(row=2,column=0)

# Récuparation du Nom et sauvegarde
#Perrine ILARY #
def saisie(val_score):
    global fin
    global Nom_saisi
    Nom_saisi=nom.get()
    print("Nom_saisi",Nom_saisi)
    f = open(os.path.dirname(os.path.abspath(__file__))+"/SCORE.TXT",'a')
    texte = str(Nom_saisi) + ';'+ str(val_score) + '\n'
    f.write(texte)

# Nouvelle partie après appuis au centre
#Perrine ILARY #
def Nouvelle_Partie():
    global canvas
    init()          #Permet de réinitilaiser le score à 0
    Pos_aleatoire()
    placer_robots()
    affich_Score(0) #Affiche 0 déplacement
    print("arrivee_pos nouveau= ",arrivee_pos)

# Affichage du score #
# Perrine ILARY #
def affich_Score (Nbr_deplacement):
    global valeur
    global val_centaine
    global val_dizaine
    global val_unite
    if (Nbr_deplacement<=9):
        car1=Nbr_deplacement
        chiffre=image_Font.crop((car1*Dx_font,0,(car1+1)*Dx_font,Dy_font)) # récupérer l'image des unités
        valeur=ImageTk.PhotoImage(image=chiffre)
        score.create_image((300,15), image=valeur) #Affiche le nombre de déplacement unitaire
    elif (Nbr_deplacement<=99):
        car1=int(Nbr_deplacement/10)
        chiffre10=image_Font.crop((car1*Dx_font,0,(car1+1)*Dx_font,Dy_font)) # récupérer l'image des dizaines
        H10=chiffre10.height
        V10=chiffre10.width
        
        car1=Nbr_deplacement-int(Nbr_deplacement/10)*10
        chiffre1=image_Font.crop((car1*Dx_font,0,(car1+1)*Dx_font,Dy_font)) # récupérer l'image des unités
        V1=chiffre1.width
        
        nombre = Image.new('RGB', (V10 + V1, H10)) #créer une nouvelle image de largeur V10+V1 et de hauteur H10
        nombre.paste(chiffre10, (0, 0))            # Concatène les
        nombre.paste(chiffre1, (V10, 0))           #deux images
        valeur=ImageTk.PhotoImage(image=nombre)    #Affiche le nombre de déplacement <100
        
        score.create_image((300,15), image=valeur)
    else:
        car1=int(Nbr_deplacement/100)
        chiffre100=image_Font.crop((car1*Dx_font,0,(car1+1)*Dx_font,Dy_font)) # récupérer l'image des dizaines
        H100=chiffre100.height
        V100=chiffre100.width
        
        tampon=Nbr_deplacement-int(Nbr_deplacement/100)*100  #supprime les centaines
        car1=int(tampon/10)   #récupère que les dizaines
        chiffre10=image_Font.crop((car1*Dx_font,0,(car1+1)*Dx_font,Dy_font)) # récupérer l'image des dizaines
        V10=chiffre10.width
        
        car1=tampon-int(tampon/10)*10    #recupère l'unité
        chiffre1=image_Font.crop((car1*Dx_font,0,(car1+1)*Dx_font,Dy_font)) # récupérer l'image des unités
        V1=chiffre1.width
        
        nombre = Image.new('RGB', (V100 + V10 + V1, H100))
        nombre.paste(chiffre100, (0, 0))
        nombre.paste(chiffre10, (V100, 0))
        nombre.paste(chiffre1, (V100+V10, 0))
        valeur=ImageTk.PhotoImage(image=nombre)
        
        score.create_image((300,15), image=valeur)

# Affichage les scores #
# Perrine ILARY #
def Affichage_scores():
    f = open(os.path.dirname(os.path.abspath(__file__))+"/SCORE.TXT",'r')
    txt = f.read()
    f.close()
    tk.messagebox.showinfo('LES SCORES', txt)
    Liste_scores = txt.split('\n')
    print(Liste_scores)

#Programme principal
bouton= tk.Button(racine, text="  Voir les SCORES    ", fg="black", bg="white",command=Affichage_scores)
canvas = tk.Canvas(racine, bg="white", width=600, height=600)
score = tk.Canvas(racine, width=600, height=30)


bouton.grid(column=0, row=0)
canvas.grid(column=0, row=1)
score.grid(column=0, row=2) #place le 0 dans la ligne du bas
cc = tk.Label(racine, text="jouez", bg = "red")
font = tkFont.Font(size=15)

init()
dessiner_terrain()
Pos_aleatoire()
creer_robots()

affich_Score (car) #Fonction à appeler pour afficher le score


canvas.bind_all('<Right>', droite)
canvas.bind_all('<Left>', gauche)
canvas.bind_all('<Up>', haut)
canvas.bind_all('<Down>', bas)
canvas.bind("<Button-1>", selection)


racine.mainloop()

print(mouvement)