# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 16:27:21 2020

@author: guife
"""

#Questão 09 da Lista 01

entrada=input('Digite a string desejada: ')

if entrada.lower()==entrada[::-1].lower():
    print('Esta string é um Palíndromo')
else:
    print('Esta string não é um Palíndromo')
