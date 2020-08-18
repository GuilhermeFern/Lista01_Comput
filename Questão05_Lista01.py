# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 14:35:45 2020

@author: guife
"""

#Questão 05 da Lista 01

teste=input('Digite aqui uma letra: ')

if teste.lower()=='a' or teste.lower()=='e' or teste.lower()=='i' or teste.lower()=='o' or teste.lower()=='u':
    print('A letra digitada é uma vogal')
else:
    print('A letra digitada é uma consoante')