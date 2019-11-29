#Cours: ITI1520
print("Dalia Sawaya: 300111681")
print("Hened Saade: 300111592")
#########################################################################
########################### Devoir5 Question2 ###########################
#########################################################################

def triangle(n):
    if n==1 :
        star=1
    else:
        star=triangle(n-1)
    print("*"*star)
    return star+1



def fun(lis,n):
    global prod
    if n==1:
        num=lis[n-1]
    else:
        if lis[n-1]>0:
            num=fun(lis,n-1)
            prod = prod*num
        else:
            num=fun(lis,n-1)
    return num

prod=1





   
        
    

    
