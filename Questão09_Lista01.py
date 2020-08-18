# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 16:01:15 2020

@author: guife
"""

#Questão 09 da Lista 01

ano=int(input('Digite o ano desejado: '))

resto=(ano%400)   

if resto==0:
    print('É um ano bissexto')
else:
    if (resto%100)==0:
        print('Não é um ano bissexto')
    elif (resto%4)==0:
        print('É um ano bissexto')
    else:
        print('Não é um ano bissexto')