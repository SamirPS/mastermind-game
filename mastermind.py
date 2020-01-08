#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 18:26:09 2018
 
@author: samir
"""
import random
import itertools

couleurchiffre=[0,1,2,3,4]

choix=int(input("1)Trouve la combi fait par l'ia  2) Crée une combi que l'ia doit trouver \n"))
while choix!=1 and choix!=2:
    choix=int(input("1)Trouve la combi fait par l'ia  2) Crée une combi que l'ia doit trouver \n"))
    
pool=[]
c=0
reussite={
        "avis":0,
        "bon":0,
        "mauvais":0,
        "nbr":0
         }

def valeur(pool,couleurchiffre):
    return [list(x) for x in itertools.permutations(couleurchiffre,4)]

def nbrdetour(niveau,reussite):
    
    reussite["nbr"]=20-5*int(niveau)
    return reussite
 
 
def creationcombi():
    return random.sample(couleurchiffre,4)	
 
 
def iacombi(pool) :
    return random.choice(pool)
 
def testliste(test):
    while len(list(set(test)))!=4 or (test[1] not in [0,1,2,3,4] or test[2]  not in [0,1,2,3,4]  or test[3]  not in [0,1,2,3,4]  or test[0]  not in [0,1,2,3,4]) :

        if test[1] not in [0,1,2,3,4] or test[2]  not in [0,1,2,3,4]  or test[3]  not in [0,1,2,3,4]  or test[0]  not in [0,1,2,3,4]:
            print("Les seuls chiffres autorise sont 0 1 2 3 4")
        else:
            print("on veut pas de doublon")

        test=demandechiffre()

   

def demandechiffre():
    return [int(x) for x in input("Rentre une combinaison : (4 chiffres sépare par des espaces de 0 a 4 qui doivent être différents )\n").split()]
  
def comparer(combi,test,reussite) :

    reussite["mauvais"],reussite["bon"]=0,0
    for i in range(4):
        if test[i] == combi[i]:
            reussite["bon"] += 1
        if  test[i] != combi[i] and test[i] in combi:
            reussite["mauvais"]+= 1
   
    if reussite["bon"]==4:
        reussite["avis"]=1
    else:
        print("vous avez ",reussite["bon"],"pions bien placés et ",reussite["mauvais"],"pions mal placés")
    return reussite
 
def eliminate(ia, reussite, combiAEliminer):
    i=0
    if reussite["mauvais"]+reussite["bon"]==4:
        for i in range(0,4):
            if ia[i] in combiAEliminer:
                ia[i]=ia[i]
            else :
                pool.remove(combiAEliminer)
                break
    elif  reussite["mauvais"]==2 and reussite["bon"]==0 or reussite["mauvais"]==0 and reussite["bon"]==2 :
        if ia[0] and ia[1] or  ia[2] and ia[3] in combiAEliminer :
            ia=ia
        else :
            pool.remove(combiAEliminer)
    return pool

if choix==1:
    niveau=input("1)Facile 2)Moyen 3) Difficile\n")
    while niveau!="1" and niveau!="2" and niveau!="3":
        niveau=input("1)Facile 2)Moyen 3) Difficile\n")
        
    nbrdetour(niveau,reussite)
    combi=creationcombi()
    print("Vous avez",reussite["nbr"],"coups possible")
    
    test=demandechiffre()
    testliste(test)
    comparer(combi,test,reussite)


    reussite["nbr"]-=1
    print("il vous reste",reussite["nbr"],"coups")
    
    while reussite["avis"]==0  and reussite["nbr"]!=0:
        reussite["nbr"]-=1
        test=demandechiffre()
        testliste(test)
        comparer(combi,test,reussite)

        if reussite["avis"] ==1:
            print("Tu es fort, tu as trouvé en",c+2,"coup")
            print(combi)
            break

        print("il reste ",reussite["nbr"],"coups")
        c=c+1
        
    if reussite["nbr"]==0 :
        print("Perdu la combi était",combi)
     
elif choix==2:
    test=demandechiffre()
    testliste(test)
    pool=valeur(pool,couleurchiffre)
    
    ia=iacombi(pool)

    comparer(test,ia,reussite)
    
    for i in range(len(pool)):
            combi=iacombi(pool)
            pool=eliminate(ia, reussite, combi)
    while reussite["avis"]==0  and c!=260: 
        ia=iacombi(pool)
        comparer(test,ia,reussite)
        if reussite["avis"] ==1:
            print("l'ia a trouve",c,"coup")
            break
        c=c+1
        
        for i in range(len(pool)):
            combi=iacombi(pool)
            pool=eliminate(ia, reussite, combi)
    if c>=260 :
        print("l'ia a perdu")
