# -*-coding utf-8 -*-

##-----Importation des Modules-----##
from Tkinter import *
from random import *


##-----Fonctions graphiques-----##
def bords():
    """Cette fonction trace la grille dans le Canvas."""
    global cote

# gauche
    dessin.create_rectangle(0,0,c+2,cote+2,fill="black")
# haut
    dessin.create_rectangle(0,0,cote+2,c+2,fill="black")
# droit
    dessin.create_rectangle(cote-c+3,10,cote+3,cote+3,fill="black")
# bas
    dessin.create_rectangle(c+3,cote+3,cote,cote-c+3,fill="black")


    

def reinit():
    """Cette fonction créer le serpent de base de 4 cases noirs."""
    global ligne, anneau,anneaucoord,pomme,a,b

    
    anneau = [0,0,0,0,0]                                        ## on initialise une liste qui contiendra les carrés représentant les anneaux du serpent
    anneaucoord =[]                                             ## on initialise une liste qui contiendra les coordonné des anneaux du serpent
    
    for k in range (5):                                     
        i = ligne//2                                          ## le premier coordonné i est au milieu du quadrillage (corespond à l'axe des ordonnés)
        j = ligne//2 + k                                        ## le premier coordonné y est au milieu du quadrillage (corespond à m'axe des abscisses)
                                                                ## on lui ajoute k à chaque fois pour que l'année se déssine une case plus loin
        
        anneaucoord.append([j,i])                               ## on ajoute les coordonné i et j dans une liste (= coordonnées d'un anneau)
                                                                ## eux même ajoutés dans une liste (= liste des coordonnés de tous les anneaux)
    for k in range (4):
        anneau[k]= dessin.create_rectangle(3+anneaucoord[k][0]*c, 3+anneaucoord[k][1]*c, 11+anneaucoord[k][0]*c, 11+anneaucoord[k][1]*c, outline="darkgreen", fill="darkgreen")
                                                                ## on cré un anneau pour chaque coordonés que l'on place dans une liste
    
    anneau[4] = dessin.create_rectangle(3+anneaucoord[4][0]*c, 3+anneaucoord[4][1]*c, 11+anneaucoord[4][0]*c, 11+anneaucoord[4][1]*c, outline="lightgreen", fill="lightgreen")

    pomme = dessin.create_rectangle(3+i*c, 3+j*c, 11+i*c, 11+j*c, outline="black", fill="red")
                                                                ## pomme dessine un carré rouge par défault au milieu du canevas

    appomme()                                                            ## il sera ensuite déplacé aléatoirement grace à la fonction appomme
    a,b=1,0
    score=0
    vies()

def appomme():
    """cette fonction fair déplace au hasard la pomme dans le jeu"""            
    global ligne, pommecoord, pomme,taille

    taille = len (anneaucoord)

    if score <50:
        x, y = randint(0,ligne-1), randint(0,ligne-1)                   ## On prend au hasard ( grace à randint) un x et un y compris dans le canevas
        pommecoord = [x,y]                                              ## on stok lescoordonnées de lapomme dans une liste
                                                                        ## ce qui sera utile lorsque le serpent rencontrera la pomme
        for w in range (taille-1):                                      ## Pour w allant de 0 à la taille du serpent
            while pommecoord == anneaucoord[w]:  ## tant que les coordonnées de la pomme sont identique à ceux d'un des anneaux du serpents
                x, y = randint(0,ligne-1), randint(0,ligne-1)           ## on prend au hasard un nouveau x, y
                pommecoord = [x,y]
            
    else:
        x, y = randint(1,ligne-2), randint(1,ligne-2)
        pommecoord = [x,y]
        
        for w in range (taille-1):                                      ## Pour w allant de 0 à la taille du serpent
            while pommecoord == anneaucoord[w]:  ## tant que les coordonnées de la pomme sont identique à ceux d'un des anneaux du serpents
                x, y = randint(2,ligne-2), randint(2,ligne-2)           ## on prend au hasard un nouveau x, y
                pommecoord = [x,y]
    
    dessin.coords(pomme,3+x*c, 3+y*c, 11+x*c, 11+y*c)              ## on change la pomme de place en fonction des coordonnés pris au hasard
                                               
    print "pomme:",pommecoord


def vies():
    """ cette fonction représente les vies"""
    global vie

    dimension = [5,15,25]
    for k in range (vie): 
        dessin1.create_oval(5,dimension[k],15,dimension[k]+10,outline="darkorange", fill="orange")
        
        
##-----Fonctions de jeu-----##
def coordonnee():
    """ cette fonction déplace le serpent dans la direction souhaité par l'utilisateur"""
    global anneaucoord, a, b, anneau, taille, drapeau, vitesse, queue
    
    if drapeau == True:
        taille = len(anneaucoord)                               ## on affecte à la variable taille le nombre des élèment que contient la liste anneaucoord
                                                                ##c'est donc le nombre d'anneaux que possède le serpent
        
        anneaucoord.append([anneaucoord[taille-1][0]+a,anneaucoord[taille-1][1]+b])
                                                                ## on ajoute à la liste des coordonnés, les coordonnés de la futur tete
                                                                ## elle sera dans la direction choisi, en fonction de a et b, variables des fonctions déplacements
                                                                ## par défaut les coordonnés sont ajoutés à la fin de la liste
                                                                ## la tete se trouve donc à la fin
        
        queue = anneaucoord [0]                                 ## on affecte à queue les coordonnés du dernière anneau du serpent
                                                                ## ce qui nous sera utile lorsque nous voudront faire grandir le serpent
        
        anneaucoord.pop(0)                                      ## on supprime le première élément de la liste
                                                                ## Pour que le serpent fasse toujours la même taille
        
        dessin.coords(anneau[taille-1],3+anneaucoord[taille-1][0]*c, 3+anneaucoord[taille-1][1]*c, 11+anneaucoord[taille-1][0]*c, 11+anneaucoord[taille-1][1]*c)
                                                                ## on déplace le carrée jaune à ses nouveaux coordonné de la liste anneaucoord
        for k in range (taille-1):
            dessin.coords(anneau[k],3+anneaucoord[k][0]*c, 3+anneaucoord[k][1]*c, 11+anneaucoord[k][0]*c, 11+anneaucoord[k][1]*c)
                                                                ## pour k allant de 0 à taille (taille du serpent)
                                                                ## on change les coordonnés des anneaux en fonction de la liste qui les contient (anneaucoord)

                                                                ## Le serpent avance donc maintenant visuellement
            
        agrandissement()                                        ## On applique la fonction agrandissement

        niveau ()
               
        verif()                                                 ## On applique la fonction vérif

        
        
        cadre.after(vitesse, coordonnee)                        ## on répète de manière continu à une vitesse constant la fonction coordonnee()
                                                                ## Ainsi le serpent est perpetuellement en mouvement

def niveau():
    """ cette fonction applique les niveaux"""
    global score,a,b,u
    
    if score <=40:                                              ## si le score est inferieur ou égal à 40
        anneaucoord.reverse()                                   ## on inverse la liste pour que la tete se trouve au début
        for h in range (taille-1):                              ## pour h allant de 0 à taille -1
            if anneaucoord[h][0]>=ligne and a == 1 and b == 0:               ## si la tete à un abscisse superieur ou égal aux ligne(si le serpent sort a droite)                   
                anneaucoord[h][0]=0                             ## on change l'abscisse de la tete pour qu'il sois 0
            elif anneaucoord[h][0]<=-1 and a == -1 and b == 0:                   ## modif pour pas se perdre
                anneaucoord[h][0]=ligne-1
            elif anneaucoord[h][1]<=-1 and a == 0 and b == -1:
                anneaucoord[h][1]=ligne-1
            elif anneaucoord[h][1]>=ligne and a == 0 and b == 1:
                anneaucoord[h][1]=0
        anneaucoord.reverse()
        
    
    if score >= 50:                                            ## modif pour reinit et tout au niveau 2
        drapeau = False
        if u != 1:
            dessin.delete(ALL)
            reinit()
            u = 1
        bords()
        verifbord()
        
    

                           
def verif():
    """cette fonction fait en sorte que le serpent meurt si il se mange"""
    global anneaucoord,drapeau
    
    for k in anneaucoord [0:taille-4:1]:                        ## Pour k allant du 3ème anneau au dernier
        
        if anneaucoord [taille-1] != k:                         ## Si la tete, le 1er anneau, a des coordonnés différents que k
            drapeau = True
        elif anneaucoord [taille-1] != k and z==1:
            drapeau = False
            z = 2                                               ## Alors le drapeau est vrai et le serpent sontinue d'avancer
        else:
            drapeau = False                                     ## Sinon le drapeau est faux le serpent s'arrette
            over()                                              ## la fonction over est appliquée

def verifbord():
    """ Cette fonction vérif que le serpent ne rentre pas dans les bords."""
    global anneaucoord,drapeau,taille
    
    if anneaucoord[taille-1][0]>=ligne-1 or anneaucoord[taille-1][0]<=0 or anneaucoord[taille-1][1]>=ligne-1 or anneaucoord[taille-1][1]<=0:
        drapeau=False
        over()
    else:
        drapeau = True

            
def over():
    """Détruit la fenettre dans laquelle se trouve le seroent pour en afficher une autre qui informe que le joueur a perdu"""
    global vie,z

    if vie == 0:
        dessin.delete(ALL)                                            ## on détruit le fenetre où se trouve le serpent
        dessin.create_text(cote//2,cote//2, text="perdu")
    else:
        vie = vie -1                                            ## si le joueur a encore des vies alors il en perd une
        dessin.delete(ALL)                                      ## un supprime tout ce qui se trouve dans dessin
        z=1
        if score >= 50:                                         ## si le joueur était dans le niveau 1 les bords se redessinent
            bords()
        dessin1.delete(ALL)                                     ## on supprime le dessin1 dans lequel sont déssinés les vies
        reinit()                                                ## on redessine le dout, le serpent et les vies qu'il reste
        appomme()
       
def agrandissement():
    """ cette fonction permet au serpent de s'agrandir si il mange la pomme"""
    global anneaucoord, pommecoord, taille, queue, score
    
    if anneaucoord[taille-1] == pommecoord:                          ## Si la tête du serpent a les même coordonnées que ceux de la pomme
        anneaucoord.insert(0,[queue [0],queue[1]])              ## Alors on ajoute à la liste des coordonnés, à le fin du serpent, les coordonnés de son ancienne queue
        anneau.insert(0,dessin.create_rectangle(3+anneaucoord[0][0]*c, 3+anneaucoord[0][1]*c, 11+anneaucoord[0][0]*c, 11+anneaucoord[0][1]*c, outline="darkgreen", fill="darkgreen"))
                                                                ## De même dans la liste des carrés, on ajoute un anneaux au serpent
        score+=10
        scoreVa.set(str(score))
        
        taille = len(anneaucoord)                               ## en recalcule la taille du serpent qui a grandit
    
        dessin.coords(anneau[taille-1],3+anneaucoord[taille-1][0]*c, 3+anneaucoord[taille-1][1]*c, 11+anneaucoord[taille-1][0]*c, 11+anneaucoord[taille-1][1]*c)        
        for k in range (taille-1):
            dessin.coords(anneau[k],3+anneaucoord[k][0]*c, 3+anneaucoord[k][1]*c, 11+anneaucoord[k][0]*c, 11+anneaucoord[k][1]*c)
                                                                ## On reassocie chaque carré à ses coordonnés
            
        appomme()                                               ## On applique la fonction pomme pour créer un nouvelle pomme et supprimer lancienne



        

def codeb(event):
    global cb
    cb=True
    
def coder(event):
    global cr
    cr=True
    
def codee(event):
    global ce
    ce=True

def scored():
    global vie, bonus, cb, cr, ce
    if cb==True and cr==True and ce==True and vie<0:
        print "HACKED"
        vie+=1
        print vie
##-----Fonctions receptionnant le gestionnaire d'événements-----##
def nouvelle_partie():  
    global vie, score   
    dessin.delete(ALL)   
    dessin1.delete(ALL)
    if vie >= 0:
        vie = 3
    if score>=0:
        score=0
        scoreVa.set(str(score))
    stop()
    reinit()
    vies()
    a,b= 1,0
    scored()
       
    print score

def stop():
  
    global drapeau
    if drapeau == False:
        drapeau = True
        coordonnee()
        bouton_pause = Button(cadre, text="Pause" , command=stop)
        bouton_pause.grid(row = 3, column = 1, sticky=S+W+E, padx=15, pady=5)
    elif drapeau == True:
        drapeau = False
        coordonnee()
        bouton_pause = Button(cadre, text="Jouer" , command=stop)
        bouton_pause.grid(row = 3, column = 1, sticky=S+W+E, padx=15, pady=5) 

def depl_bas(event):
    """Cette fonction fait tourner le serpent en bas."""
    global a,b, drapeau
    
    drapeau = False
    
    if b == -1 :            #"""and vie !=0:"""                                                 ## si b est égale à -1 donc si le déplacement en cours est direction haut
        if drapeau == False:
            drapeau = True
            a=0
            b=-1                                                ## alors b est toujours égale à -1, le serpent continu à aller vers le haut
                                                                ## Le serpent ne peux pas revenir sur lui même

    else:                                                       ## si b est différent de -1, donc que le déplacement en cours est direction gauche ou droite
        drapeau = True
        a=0
        b=1                                                     ## alors b = 1 et le serpent se dirigera vers le bas


def depl_haut(event):
    """Cette fonction fait tourner le serpent en haut."""
    global a,b, drapeau
    
    drapeau = False
    
    if b == 1:
        if drapeau == False: #"""and vie !=0:"""
            drapeau = True
            a=0
            b=1
    else:
        drapeau = True
        a=0
        b=-1
            
   
def depl_gauche(event):
    """Cette fonction fait tourner le serpent à gauche."""
    global a,b, drapeau
    
    drapeau = False
    
    if a == 1:
        if drapeau == False: #"""and vie !=0:"""
            drapeau = True
            a=1
            b=0
    else:
        drapeau = True
        a=-1
        b=0
        


def depl_droite(event):
    """Cette fonction fait tourner le serpent à droite."""
    global a,b, drapeau
    
    drapeau = False
    
    if a == -1:
        if drapeau == False: #"""and vie !=0:"""
            drapeau = True
            a=-1
            b=0
    else:
        drapeau = True
        a=1
        b=0

    
##-----Les variables-----##
cote = 200                                           ## Dimensions de la grille


c = 10                                               ## Dimensions des cellules
ligne = cote//c                                      ## Nombre de cellules en hauteur

i = j = ligne//2                                    ## coordonnés de la cellule centrale

vitesse = 100                                        ## vitesse de déplacement de base du serpent

a,b = 1,0                                            ## direction de déplacement de base du serpent: vers la droite

score = 0                                            ## cette variable compte le score au fur et à mesure

vie = 3                                              ## cette  variable compte le nombre de vies du joueur
    
drapeau = False                                      ## le drapeau est baissé, le serpent est immobile au début
u=0

z = 0



cb = False
cr = False
ce = False

##-----Création de la fenêtre-----##
cadre = Tk()                                         ## création de la fenêtre qui se nomme cadre
cadre.title("Snake")                                 ## titre de la fenêtre: Snake


##-----Création et placement des boutons-----##
bouton_quitter = Button(cadre, text="Quitter", command=cadre.quit)
                                                     ## boutton qui permet de quitter d'un clic de souris la fenêtre
bouton_quitter.grid(row = 4, column = 2, sticky=S+W+E, padx=15, pady=5)

bouton_nouvelle_partie = Button(cadre, text="Nouvelle Partie", command=nouvelle_partie)
bouton_nouvelle_partie.grid(row = 3, column = 2, sticky=S+W+E, padx=15, pady=5) 

bouton_stop = Button(cadre, text="Jouer", command=stop)
bouton_stop.grid(row = 3, column = 1, sticky=S+W+E, padx=15, pady=5)

  

##-----Création d'une zone de texte-----##
texte1 = Label(cadre, text="Bienvenue au jeu de snake.")
texte1.grid(row = 0, column = 1, columnspan = 2, sticky = W+E)

texte2 = Message(cadre, text=" Utilisez les flêches de votre clavier pour vous déplacer."
                             " Appuyez sur la barre d'espace pour commencer ou mettre en pause.")
texte2.grid(row = 1, column = 0, rowspan = 2)

texte4 = Label(cadre, text ="Vies restantes:")
texte4.grid(row = 1, column=3, sticky = N + E +W, pady = 5)

texte3 = Label(cadre, text='Score:  ')
texte3.grid(row=4,column=0)

scoreVa = StringVar()
Score = Entry(cadre, textvariable=scoreVa)
Score.grid(row=4,column=1)
scoreVa.set('0')


##-----Création d'un canevas et d'une grille dans le canevas-----##
dessin = Canvas(cadre, bg="white", width=cote+1, height=cote+1)
dessin.grid(row = 1, column = 1, columnspan = 2, rowspan = 2, pady=5)

dessin1 = Canvas(cadre,bg="white",width = 20, height =35)
dessin1.grid(row = 2,column = 3)

cadre.bind("<b>", codeb) # Bénouska
cadre.bind("<r>", coder) # Ramonlejambon
cadre.bind("<e>", codee) # Embabalafuerza


##-----Programme principal-----##

reinit()

cadre.bind_all("<Up>",depl_haut)                     ## permet l'interaction joueur / programme grace au clavier
cadre.bind_all("<Down>",depl_bas)
cadre.bind_all("<Left>",depl_gauche)
cadre.bind_all("<Right>",depl_droite)
"""cadre.bind_all("<space>",start_stop)""" # Etant donné que l'on assignait cette command à un event
                                           # nous ne pouvions réenclencher la fonction nouvelle partie(event)
                                           #  un bouton graphique fonctionne contrairement au bouton
                                           # physique.



cadre.mainloop()
cadre.destroy()

        
