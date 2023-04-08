# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 11:31:45 2021

@author: noamb
"""
import csv
import matplotlib.pyplot as plt

with open('arrondissements.csv', mode='r') as f:
    L = list(csv.reader(f, delimiter = ';'))
    
for i in range(1, len(L)):
    a = eval(L[i][9])['coordinates'][0]
    x = []
    y = []  
    for cos in a:
        x.append(cos[0])
        y.append(cos[1])
      
    plt.savefig('carte paris.png')
    plt.axis('off')
    plt.plot(x,y,lw=1,color='b')
    plt.title('Carte de Paris ')
