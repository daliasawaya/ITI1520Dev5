#Cours: ITI1520
print("Dalia Sawaya: 300111681")
print("Hened Saade: 300111592")
#########################################################################
########################### Devoir5 Question2 ###########################
############################# PARTIE A et B #############################
#########################################################################


#############################   PARTIE A   #############################


def triangle(n):
    '''
    (int)->int
    fonction recursive qui imprime triangle d'etoile de hauteur n
    '''
    if n==1: #cas qui termine la recursivite 
        star=1
    else: #si n n'est pas 1
        star=triangle(n-1) #appelle fonction avec n-1
    print("*"*star) #imprime * fois ce qui est retourne avant
    return star+1

#interagit avec usager et demande pour num
print('QUESTION 2 PARTIE A -- triangle ')
num = int(input('Entrez un entier pour hauteur du triangle: '))
triangle(num)


#############################   PARTIE B   #############################


print('QUESTION 2 PARTIE B -- produit de liste')
print('appelle la fonction prodListePos_rec')

def prodListePos_rec(l, n):
    '''
    (list,int)->int
    fonction qui retourne produit des elements >0 d'une liste
    '''
    if n==0 : #cas 1 qui termine la recursivite, se passe seulement si l[0]<=0
        p=1
    elif n==1 and l[0]>0: #cas 2 qui termine la recursivite 
        p = l[0]
    else: #si les 2 cas ne sont pas verifies, (reste encore des elements dans liste)
        if l[n-1]>0 : #si l'element est>0, appelle fonction avec prochain element
            p = prodListePos_rec(l,n-1) * l[n-1]
            #et multiplie le resultat avec l'element precedent
        else : #si l'element est<0, appelle fonction avec prochain element
            p = prodListePos_rec(l,n-1) #mais ne multiplie pas avec cet element
    return p 







    

        
    

        





   
        
    

    
