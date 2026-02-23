#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

from time import localtime 
from math import sqrt
from datetime import datetime
from sys import argv

### Functions

def gen_candidat():
    increment = (4,2,4,2,4,6,2,6)
    j = 0
    p = 7  
    while True:
        if j == 8: j = 0
        p = p + increment[j]
        j += 1
        yield p

def n_prems(num:int):
    compteur = 1
    prem_test = []
    premiers = [2,3,5,7]
    i = 3
    c = gen_candidat()
    nb_test = 0

    while compteur < num-3:
        # Sélection du nombre à tester que l'on appelle : le "candidat".
        # On suppose arbitrairement qu'il est premier : check = True.
        candidat = next(c)
        check = True    

        # Tests pour savoir si le candidat est premier.
        # On fait le teste racine, qui s'il réussit, nous indique que le candidat n'est pas premier.
        # Il permet également d'augmenter la liste de nombres premier test.
        if premiers[i] == sqrt(candidat):
            nb_test += 1 
            prem_test.append(premiers[i])
            check = False
            i += 1 
        else: 
            for r in prem_test: 
                nb_test += 1  
                if candidat % r == 0:  
                    check = False
                    break
        if check:
            premiers.append(candidat) 
            compteur += 1     

    return premiers,nb_test

### Main

if __name__ == "__main__":

    if len(argv)>1:
        numero = int(argv[1])
    else:
        numero = int(input("Quel nombre premier voulez-vous ? Le numéro : "))

    time = datetime.now()
    time1 = 3600*time.hour + 60*time.minute + time.second

    premiers,nb_test = n_prems(numero)

    time = datetime.now()
    time2 = 3600*time.hour + 60*time.minute + time.second
    secondes = time2 - time1

    print(f"\nLe {numero}ème nombre premier est {premiers[numero-1]}")
    print(f"Nombre de tests : {nb_test}")
    print(f"Temps (s) = {secondes}")

    if (secondes):
        testsec = round(nb_test / secondes)
        print(f"Tests/s : {testsec}")


