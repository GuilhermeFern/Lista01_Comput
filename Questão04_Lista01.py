# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 14:12:19 2020

@author: guife
"""

#Questão 04 da Lista 01

num=input('Digite os três números com espaços entre eles: ')

num1=int(num[0])
num2=int(num[2])
num3=int(num[4])

lista=[num1,num2,num3]

print(min(lista),lista[int(len(lista)/2)],max(lista))