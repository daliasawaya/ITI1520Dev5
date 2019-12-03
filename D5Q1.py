#Nom: Dalia Sawaya
#Num Etudiant: 300111681
#Cours: ITI1520
print("Dalia Sawaya 300111681")
print("Hened Saade 300111592")
#########################################################################
########################### Devoir5 Question1 ###########################
#########################################################################
 
class Personne:
    '''
    represente une classe Personne
    '''
    
    #methode qui initialise les personnes et les donne leur nom, prenom et ID
    def __init__(self, nom, prenom, identifiant):
        '''
        (str,str, int)->None
        initialise les attributs de la classe Personne
        '''
        self.nom = nom
        self.prenom = prenom
        self.identifiant = identifiant


    #methode qui nous permet de retourner ce qu'on veut quand on essaye d'imprimer une personne
    #comme ca, on n'imprime pas l'addresse dans la memoire
    def __repr__(self):
        '''
        (Personne)->str
        retourne une representation de l'objet
        '''
        #cree un string de toute l'info d'une personne
        strInfo = "Nom: "+self.nom+", Prenom: ",self.prenom,+", Indentifiant: "+str(self.identifiant)
        return strInfo


    #methode qui verifie si 2 diff personnes ont le meme nom, prenom et ID quand on fait ==
    #au lieu de retourner l'addresse dans la memoire
    def __eq__(self, autre):
        '''
        (Personne, Personne)->bool
        self == autre si le nom et le prenom sont les memes
        '''
        if self.nom != autre.nom : #si les nom des 2 objets sont egalent
            return False #retourne False
        if self.prenom != autre.prenom : #si les prenom des 2 objets son egale
            return False #retourne False
        if self.identifiant != autre.identifiant : #si les ID des 2 objets son egale
            return False #retourne False
        return True #retourne False


#classe pour les etudiants qui vient de classe Personne
class Etudiant(Personne):
    '''
    represente une classe Etudiant
    '''
     # solde est un attribut de la classe Etudiant
     # cours est une liste de cours (une liste de chaine de caracteres)


    #methode qui initialise les etudiants et les attribut leur solde et liste de cours
    def __init__(self, nom, prenom, identifiant, solde, cours):
        #utilise classe Personne pour donner nom, prenom et ID
        Personne.__init__(self, nom, prenom, identifiant) 
        self.solde = solde
        self.cours = cours


    #methode qui nous permet de retourner ce qu'on veut quand on essaye d'imprimer un etudiant
    #comme ca, on n'imprime pas l'addresse dans la memoire
    def __repr__(self):
        '''
        (Personne)->str
        retourne une representation de l'objet
        '''

        #cree un string avec nom, prenom et ID d'un etudiant
        strInfo1 = "Nom:"+self.nom+", Prenom:"+self.prenom+", Indentifiant:"+str(self.identifiant)

        #creer un string de la liste des cours
        strList = ''
        for k in self.cours:
            strList = strList + ' ' +k

        #cree un string avec solde et le string des cours
        strInfo2 = ", Solde:"+str(self.solde)+", Liste de cours:"+strList

        #cree string totale avec toute info d'etudiant
        strInfo = strInfo1 + strInfo2
        
        return strInfo


    #methode qui ajoute un cours a la liste de cours d'un etudiant seulement si solde=0
    def ajouterCours(self, nomCours):
        if self.solde==0: #verifie si solde est 0
            (self.cours).append(nomCours) #si oui, ajoute le cours et retourne True
            return True
        return False #si non, retourne False
     
     
#classe pour les employes qui vient de classe Personne
class Employe(Personne):
    '''
    represente un employe
    '''
    
    # tauxHoraire est un attribut de la classe Employe

    
    #methode qui initialise les employes et les attribut leur taux horaire
    def __init__(self, nom, prenom, identifiant, tauxHoraire):
        #utilise classe Personne pour donner nom, prenom et ID
        Personne.__init__(self, nom, prenom, identifiant)
        self.tauxHoraire = tauxHoraire


    #methode qui nous permet de retourner ce qu'on veut quand on essaye d'imprimer un employe
    #comme ca, on n'imprime pas l'addresse dans la memoire
    def __repr__(self):
        '''
        (Personne)->str
        retourne une representation de l'objet
        '''
        #cree et retourne un grand string avec toute l'info d'un employe
        strInfo1 = "Nom:"+self.nom+", Prenom:"+self.prenom+", Indentifiant:"+str(self.identifiant)
        strInfo2 = ", Taux Horaire:"+str(self.tauxHoraire)
        strInfo = strInfo1 + strInfo2
        return strInfo


    #methode qui calcule et retourne le salaire d'un employe
    def calculerSalaire(self, numHeures, tauxHoraire) :
        return numHeures * tauxHoraire


#classe qui gere le campus
class Gestion:
    #cree 2 listes vides, une pour tous les etudiants et une pour tous les employes
    listEtudiant = []
    listEmploye = []


    #methode qui ajoute un etudiant a la liste des etudiants
    def ajouterEtudiant(self):
        '''
        none -> bool
        ajouter des etudiants dans une liste d'etudiant
        '''
        #interagit avec usager et prend l'info sur l'etudiant (nom, prenom, ID et solde)
        name = str(input("Entrez le nom: "))
        Fname = str(input("Entrez le prenom: "))
        ID = int(input("Entrez l'identifiant: "))
        sold = float(input("Entrez le solde: "))
        
        #cree liste vide pour les cours, demande pour les cours et les separe par les virgules
        cours = []
        cours_str = input("Entrez cours separes par virgules: ")
        cours_list  = cours_str.split(",")
        
        #ajoute les cours entres par l'usager a la liste de cours
        for c in cours_list:
            cours.append(c)
            
        #demande si usager veut ajouter autre cours
        add = str(input("Veux-tu ajouter un autre cours? entrez 'oui' ou 'non': "))
        if add == 'oui': #si usager dit oui, demande quel cours
            nouvCours = str(input("Entrez le cours a ajouter: "))
            #cree cet etudiant
            etudiant = Etudiant(name, Fname, ID, sold, cours)
            #appelle methode ajouterCours avec cet etudiant (verifier si solde est 0)
            if Etudiant.ajouterCours(etudiant, nouvCours): #si methode ajouterCours retourne True
                print("Le cours a ete ajoute.")
            else: #si methode ajouterCours retourne False
                print("Vous devez payer votre solde avant d'ajouter un cours.")
        else : #si l'usager dit non pour ajouter un cours
            print("D'accord, on n'ajoute rien, maintenant pour la prochaine etape.")

        #cree etudiant avec toute info
        etudiant = Etudiant(name, Fname, ID, sold, cours)

        #verifie si etudiant existe dans liste d'etudiants deja
        for i in Gestion.listEtudiant :
            if i == etudiant : #si oui, retourne False
                return False
        Gestion.listEtudiant.append(etudiant) #si non, ajoute cet etudiant dans liste et retourne True
        return True
            
        
    #methode qui ajoute un employe a la liste des employe
    def ajouterEmploye(self):
        '''
        none -> bool
        ajouter des etudiants dans une liste d'etudiant
        '''

        #interagit avec usager et prend l'info sur l'employe (nom, prenom, ID et tauxHoraire)
        name = str(input("Entrez le nom: "))
        Fname = str(input("Entrez le prenom: "))
        ID = int(input("Entrez l'identifiant: "))
        taux = float(input("Entrez le taux horaire: "))

        #cree cet employe
        employe = Employe(name, Fname, ID, taux)

        #verifie si employe existe dans liste d'employes deja
        for j in Gestion.listEmploye :
            if j == employe : #si oui, retourne False
                return False
        Gestion.listEmploye.append(employe) #si non, ajoute cet employe dans liste et retourne True
        return True

        
    #methode qui compte combien d'etudiants n'ont pas payer leur solde
    def SoldeNonPaye(self):
        '''
        none -> int
        retourner le nombre des etudiants qui ont un solde non paye
        '''

        #initialise compteur a 0
        compteur = 0

        #passe a travers liste des etudiants
        for m in Gestion.listEtudiant :
            if m.solde!=0: #chaque fois qu'on trouve un etudiant qui n'a pas payer leur solde
                compteur+=1 #on incremente le compteur
        return compteur
                

    #methode qui retourne le salaire de l'employe
    def salaireInd(self, employe, heures):
        '''
        (str) -> float
        retourne le salaire d'un employe
        '''

        #verifie si l'employe est dans la liste d'employes
        if employe in Gestion.listEmploye:
            #si oui, calcule et retourne son salaire
            salaire = Employe.calculerSalaire(employe, heures, employe.tauxHoraire )
            return salaire
        else: #si il n'est pas dans la liste, retourne 0
            return 0


#program principal
g = Gestion()


print("Ajoutez des etudiants.")

# Ajouter des etudiants
if g.ajouterEtudiant() :
    print("Etudiant ajoute avec succes.")
else:
    print("Etudiant existe deja dans le systeme, on ne la pas ajouter.")
if g.ajouterEtudiant() :
    print("Etudiant ajoute avec succes.")
else:
    print("Etudiant existe deja dans le systeme, on ne la pas ajouter.")



# Ajouter des employes
print("Ajouter des employes.")
if g.ajouterEmploye() :
    print("Employer ajoute avec succes.")
else:
    print("Employer existe deja dans le systeme, on ne la pas ajouter.")
if g.ajouterEmploye() :
    print("Employer ajoute avec succes.")
else:
    print("Employer existe deja dans le systeme, on ne la pas ajouter.")
#g.ajouterEmployes()



# Afficher le nombre des employes et des etudiants
print("il y a: ", len(Gestion.listEtudiant), " etudiants.")
print("il y a: ", len(Gestion.listEmploye), " employes.")


# Afficher le nombre des etudiants qui ont un solde a payer
print("il y a ", g.SoldeNonPaye(), "etudiants qui n'ont pas paye leur solde.")


# Afficher les salaires de tous les employes
for e in Gestion.listEmploye:
    heure = int(input("Entrez le nombre des heures pour employe " + e.prenom + " " + e.nom + ": "))
    print('Le salaire de:', e.nom, e.prenom, 'est:', g.salaireInd(e, heure), '$.')

#Afficher toute la Gestion
print("Toute la gestion: ")
print(Gestion.listEtudiant)
print(Gestion.listEmploye)
