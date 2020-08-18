# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 14:56:12 2020

@author: guife
"""

#Questão 07 da Lista 01

posicao=input('Qual a posição do tabuleiro desejada? ')

resto=int(posicao[1])

if posicao[0].lower()=='a' or posicao[0].lower()=='c' or posicao[0].lower()=='e' or posicao[0].lower()=='g':
    if (resto%2)==0:
        print('O quadrado sugerido é Branco')
    else:
        print('O quadrado sugerido é Preto')
else:
    if (resto%2)==0:
        print('O quadrado sugerido é Preto')
    else:
        print('O quadrado sugerido é Branco')