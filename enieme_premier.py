#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#################################################################
#                                                               #
# Auteur :  Boris Mélène                                        #
# Date :    27/06/2020                                          #
# Version : 1.6.1 Linux                                         #
# But : Calcule le n-ème nombre premier et retourne le nombre   #
#       de tests nécessaires pour arriver au résultat.          #
#                                                               #
#                                                               #
#                                                               #
#                                                               #
# Mises-à-jour :                                                #
#  1.3.5 Version initiale. Copie et mise-a-jour pour Linux de   #
#  la version pour Windows.                                     #
#  1.4.0 Réduit le nombre de valeurs a tester.                  #
#  1.4.1 Réarrange les declarations de variables.               #
#  1.4.2 Conversion en Python                                   #
#  1.5.0 Mise-à-jour pour Python 3                              #
#  1.6.0 Utilisation de générateurs                             #
#  1.6.1 Added utf-8 encoding                                   #
#                                                               #
#                                                               #
#################################################################
#

from time import localtime 
from math import sqrt
from datetime import datetime

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


### Main

compteur = 1
nb_test = 0
prem_test = []
premiers = [2,3,5,7]
i = 3
c = gen_candidat()

numero = int(input("Quel nombre premier voulez-vous ? Le numéro : "))

time = datetime.now()
time1 = 3600*time.hour + 60*time.minute + time.second

while compteur < numero-3:
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

time = datetime.now()
time2 = 3600*time.hour + 60*time.minute + time.second
secondes = time2 - time1

print(f"\nLe {numero}ème nombre premier est {premiers[numero-1]}")
print(f"Nombre de tests : {nb_test}")
print(f"Temps (s) = {secondes}")

if (secondes):
    testsec = round(nb_test / secondes)
    print(f"Tests/s : {testsec}")


