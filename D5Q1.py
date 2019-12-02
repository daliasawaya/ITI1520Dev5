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
    
    def __init__(self, nom, prenom, identifiant):
        '''
        (str,str, int)->None
        initialise les attributs de la classe Personne
        '''
        self.nom = nom
        self.prenom = prenom
        self.identifiant = identifiant

    def __repr__(self):
        '''
        (Personne)->str
        retourne une representation de l'objet
        '''
        strInfo = self.nom + self.prenom + str(self.identifiant)
        return strInfo

    def __eq__(self, autre):
        '''
        (Personne, Personne)->bool
        self == autre si le nom et le prenom sont les memes
        '''
        if self.nom != autre.nom :
            return False
        if self.prenom != autre.prenom :
            return False
        if self.identifiant != autre.identifiant :
            return False
        return True



class Etudiant(Personne):
    '''
    represente une classe Etudiant
    '''
     # solde est un attribut de la classe Etudiant
     # cours est une liste de cours (une liste de chaine de caracteres)

    def __init__(self, nom, prenom, identifiant, solde, cours):
        Personne.__init__(self, nom, prenom, identifiant)
        self.solde = solde
        self.cours = cours
     
    def __repr__(self):
        '''
        (Personne)->str
        retourne une representation de l'objet
        '''
        strInfo = self.nom+self.prenom+str(self.identifiant)+'_'+str(self.solde)+'_'+str(len(self.cours))
        return strInfo

    def ajouterCours(self, nomCours):
        if self.solde==0:
            (self.cours).append(nomCours)
            return True
        return False
     
     

class Employe(Personne):
    '''
    represente un employe
    '''
    # tauxHoraire est un attribut de la classe Employe
    
    def __init__(self, nom, prenom, identifiant, tauxHoraire):
        Personne.__init__(self, nom, prenom, identifiant)
        self.tauxHoraire = tauxHoraire

    def __repr__(self):
        '''
        (Personne)->str
        retourne une representation de l'objet
        '''
        strInfo = self.nom+self.prenom+str(self.identifiant)+'_'+str(self.tauxHoraire)
        return strInfo

    def calculerSalaire(self, numHeures, tauxHoraire) :
        return numHeures * tauxHoraire




class Gestion:
    listEtudiant = []
    listEmploye = []
 
    def ajouterEtudiant(self):
        '''
        none -> bool
        ajouter des etudiants dans une liste d'etudiant
        '''
        name = str(input("Entrez le nom: "))
        Fname = str(input("Entrez le prenom: "))
        ID = int(input("Entrez l'identifiant: "))
        sold = float(input("Entrez le solde: "))

        cours = []
        cours_str = input("Entrez cours separes par virgules: ")
        cours_list  = cours_str.split(",")
        
        for c in cours_list:
            cours.append(c)

        add = str(input("Veux-tu ajouter un autre cours? entrez 'oui' ou 'non': "))
        if add == 'oui':
            nouvCours = str(input("Entrez le cours a ajouter: "))
            etudiant = Etudiant(name, Fname, ID, sold, cours)
            if Etudiant.ajouterCours(etudiant, nouvCours):
                print("Le cours a ete ajoute.")
            else:
                print("Vous devez payer votre solde avant d'ajouter un cours.")
        else :
            print("D'accord, on n'ajoute rien, maintenant pour la prochaine etape.")

        etudiant = Etudiant(name, Fname, ID, sold, cours)

        for i in Gestion.listEtudiant :
            if i == etudiant :
                return False
        Gestion.listEtudiant.append(etudiant)
        return True
            
        

    def ajouterEmploye(self):
        '''
        none -> bool
        ajouter des etudiants dans une liste d'etudiant
        '''
        name = str(input("Entrez le nom: "))
        Fname = str(input("Entrez le prenom: "))
        ID = int(input("Entrez l'identifiant: "))
        taux = float(input("Entrez le taux horaire: "))

        employe = Employe(name, Fname, ID, taux)

        for j in Gestion.listEmploye :
            if j == employe :
                return False
        Gestion.listEmploye.append(employe)
        return True
        
    
    def SoldeNonPaye(self):
        '''
        none -> int
        retourner le nombre des etudiants qui ont un solde non paye
        '''
        compteur = 0
        for m in Gestion.listEtudiant :
            if m.solde!=0:
                compteur+=1
        return compteur
                

    def salaireInd(self, employe, heures):
        '''
        (str) -> float
        retourne le salaire d'un employe
        '''
        if employe in Gestion.listEmploye:
            salaire = Employe.calculerSalaire(employe, heures, employe.tauxHoraire )
            return salaire
        else:
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
    heure = int(input("Entrez le nombre des heures pour employe " + e.prenom + " " + e.nom + " "))
    print('Le salaire de:', e.nom, e.prenom, 'est:', g.salaireInd(e, heure), '$.')

#Afficher toute la Gestion
print("Toute la gestion: ")
print(Gestion.listEtudiant)
print(Gestion.listEmploye)
