import pandas as pd




def lire_donnees_Admin(fichier_csv):
# Spécifiez le chemin vers votre fichier CSV
    fichier_csv = pd.read_csv('Administrateur.csv', header=None)

    tableau = fichier_csv.values
    # Afficher le tableau
    print(tableau)
    listeNumeroAdmin = []
    listeNom = []
    listeMotDePasse = []
    compteur = len(tableau)
    for i in range(compteur):
        listeNumeroAdmin.append(tableau[i][1])
        listeNom.append(tableau[i][0])
        listeMotDePasse.append(tableau[i][2])

    return listeNumeroAdmin, listeNom, listeMotDePasse



def rechercherAdmin(listeNumeroAdmin,listeNom,listeMotDePasse,numeroRecherche):
    compteur = len(listeNumeroAdmin)
    for i in range(compteur):
        if(listeNumeroAdmin[i]==numeroRecherche):
            return(listeNom[i], listeMotDePasse[i])
    return (-1,-1)
""" 
numeroRecherche  = 333

nom, motdePasse = rechercherAdmin(listeNumeroAdmin, listeNom, listeMotDePasse, numeroRecherche)   

if(nom!= -1 and motdePasse!= -1):
    print(nom,motdePasse)
else:
    print("erreur !")
"""