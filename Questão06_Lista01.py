# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 14:40:25 2020

@author: guife
"""

#Questão 06 da Lista 01

entrada=input('Digite aqui o mês de sua preferência: ')

if entrada.lower()=='janeiro' or entrada.lower()=='março' or entrada.lower()=='maio' or entrada.lower()=='julho' or entrada.lower()=='agosto' or entrada.lower()=='outubro' or entrada.lower()=='dezembro':
    print('Este mês possui 31 dias')
elif entrada.lower()=='abril' or entrada=='junho' or entrada=='setembro' or entrada=='novembro':
    print('Este mês possui 30 dias')
elif entrada.lower()=='fevereiro':
    print('Este mês possui 28 ou 29 dias')
else:
    print('Este mês não é válido')