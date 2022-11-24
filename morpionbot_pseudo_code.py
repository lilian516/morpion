# on importe la fonction random
# Debut
# on créé la classe morpion

    #on définit la fonction init
        #on créé l'objet tableau

    # on définit la fonction creer_tableau qui prends en paramètre l'objet tableau 
        #pour i de 0 à 3
            #on crée le tableau ligne
            #pour j de 0 à 3
                #on ajoute le caractère '-' au tableau ligne
            #on ajoute le tableau ligne à tableau
    
    #on définit une fonction mettre_signe qui prends en parametre l'objet tableau, la ligne, la colonne et le joueur
        #si ligne est plus grand que 3 et colonne est plus grand que 3
            #alors on demande au joueur quel ligne et quel colonne il choisit et on les stocke dans les variables ligne et colonne
        #sinon
            #alors on ajoute le signe au coordonnées choisient

    #on définit la fonction victoire_joueur qui prends en parametre le tableau
        #win est égal à None
        #n est égal à longueur de tableau 

        #on regarde les lignes
        #pour i de 0 à n
            #win est égale à True
            #pour j de 0 à n
                #si tableau aux coordonées i et j est différent de player
                    #alors win est égal à False
            #si win est égal à True
                #alors on retourne win
        
        #on regarde les colonnes
        #pour i de 0 à n
            #win est égale à True
            #pour j de 0 à n
                #si tableau aux coordonées j et i est différent de player
                    #alors win est égal à False
            #si win est égal à True
                #alors on retourne win
        
        #on regarde les diagonales
        #win est égale à True
        #pour i de 0 à n
            #si tableau aux coordonées i et i est différent de player
                    #alors win est égal à False
        #si win est égal à True
            #alors on retourne win
        #win est égale à True
        #pour i de 0 à n
            #si tableau aux coordonées i et n-1-i est différent de player
                    #alors win est égal à False
        #si win est égal à True
            #alors on retourne win
        #on retourne False
        #pour ligne dans tableau
            #pour item dans ligne
                #si item est égal à '-'
                    #alors on retourne False
        #retourne True

        #on définit la fonction tableau_remplit qui prendt en parametre le tableau
            #pour ligne dans tableau
                #pour item dans ligne
                    #si item est égal à '-'
                        #alors on retourne False
            #on retourne True

        #on définit la fonction tour_joueur_suivant qui prendt en parametre un tableau et un joueur
            #on retourne x si player est égal à 0 sinon on retourne 0

        #on définit la fonction afficher_tableau avec en parametre tableau
            #pour ligne dans tableau
                #pour item dans ligne
                    #afficher item
        
        #on définit la fonction start
            #on appelle la fonction creer_tableau
            #on définit la variable tour qui est égale à 1
            #Tant que True 
                #afficher Tour du joueur x 
                #appeler la fonction afficher_tableau
                # demander au joueur la postion de son signe
                # mettre le signe aux bonnes coordonnées en appelant la fonction mettre_signe
                # on regarde si un joueur a gagné
                #si la fonction victoire_joueur est égal à True 
                    #alors on affiche Joueur x ou 0 à gagné le match
                #si la fonction tableau_remplit est égal à True
                    #affiché Match Nul !                
                # passer au tour suivant en appelant la fonction tour_joueur_suivant
                #on appelle la fonction tour_bot qui prendt en paramètre la ligne la colonne le player et le tour
                #tour est égal à tour +1
                # on regarde si le bot a gagné
                #si la fonction victoire_joueur est égal à True 
                    #alors on affiche Joueur 0 à gagné le match
                #si la fonction tableau_remplit est égal à True
                    #affiché Match Nul ! 
                # passer au tour suivant en appelant la fonction tour_joueur_suivant
            #on affiche la tableau à la fin du match an appelant la fonction afficher_tableau

#on commence le match
#morpion est égal à morpion()
#on éxecute la fonction start
#Fin