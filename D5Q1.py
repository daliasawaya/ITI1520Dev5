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
        # A completer

    def __repr__(self):
        '''
        (Personne)->str
        retourne une representation de l'objet
        '''
        # A completer

    def __eq__(self, autre):
        '''
        (Personne, Personne)->bool
        self == autre si le nom et le prenom sont les memes
        '''
        # A completer

class Etudiant(Personne):
    '''
    represente une classe Etudiant
    '''
     # solde est un attribut de la classe Etudiant
     # cours est une liste de cours (une liste de chaine de caracteres)
     
     # methodes
     
     # A completer
    

class Employe(Personne):
    '''
    represente un employe
    '''
    # tauxHoraire est un attribut de la classe Employe
    
    # methodes

    # A completer


class Gestion:
    listEtudiant = []
    listEmploye = []
 
    def ajouterEtudiant(self):
        '''
        none -> bool
        ajouter des etudiants dans une liste d'etudiant
        '''
        # Completer

    def ajouterEmploye(self):
        '''
        none -> bool
        ajouter des etudiants dans une liste d'etudiant
        '''
        # Completer
    
    def SoldeNonPaye(self):
        '''
        none -> int
        retourner le nombre des etudiants qui ont un solde non paye
        '''
        # Completer

    def salaireInd(self, employe, heures):
        '''
        (str) -> float
        retourne le salaire d'un employe
        '''
        # Completer


#program principal
g = Gestion()
print("Ajoutez des etudiants.")
# Ajouter des etudiants
g.ajouterEtudiant()
g.ajouterEtudiant()

# Ajouter des employes
print("Ajouter des employes.")
g.ajouterEmploye()
g.ajouterEmploye()
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
