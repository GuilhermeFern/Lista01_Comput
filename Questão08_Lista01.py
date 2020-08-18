# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 15:23:27 2020

@author: guife
"""

#Questão 08 da Lista 01

dia_inf=input('Informe a data desejada: ')

dia=int(dia_inf[0:2])
mes=dia_inf[6:]

if mes.lower()=='janeiro' or mes.lower()=='fevereiro':
    print('Verão')
elif mes.lower()=='abril' or mes.lower()=='maio':
    print('Outono')
elif mes.lower()=='julho' or mes.lower()=='agosto':
    print('Inverno')
elif mes.lower()=='outubro' or mes.lower()=='novembro':
    print('Primavera')
elif mes.lower()=='março':
    if dia<20:
        print('Verão')
    else:
        print('Outono')
elif mes.lower()=='junho':
    if dia<20:
        print('Outono')
    else:
        print('Inverno')
elif mes.lower()=='setembro':
    if dia<21:
        print('Inverno')
    else:
        print('Primavera')
elif mes.lower()=='dezembro':
    if dia<20:
        print('Primavera')
    else:
        print('Verão')