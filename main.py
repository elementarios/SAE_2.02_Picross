Vide = "VIDE"
Noir = "NOIR" #les different etat du picross
Croix = "Croix"

taille=0
plateau=[[]]

def init():
    global taille
    global plateau
    global Vide
    taille = int(input("la taille du plateau:"))
    plateau=[[Vide for i in range(taille)]for j in range(taille)]

def affichage():
    """affiche le plateau de maniere "classe"
    """
    global plateau
    global taille
    for i in range(taille):
        ligne=""
        for j in range(taille):
            ligne+=str(plateau[i][j])+" " #la commande str transforme en string 
        print(ligne)


init()
affichage()

def verification(ligne,indice):
    """retourne True si la ligne respecte les consigne donnes par les indices

    Args:
        ligne (tableau): correspond a une ligne/colonne
        indice (tableau): correspond au regle 
    """
    motif=0
    cpt=0

