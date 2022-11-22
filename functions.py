from os import system
from data import *
fajlnev='cégek.txt'

def fajlbetoltes():
    file=open(fajlnev, 'r', encoding='utf-8')
    for row in file:
    #row->Kovács Béla;7.56\n
        darabolt=row.strip().split(';')
        #print(darabolt)
        nevek.append(darabolt[0])
        ratingek.append(float(darabolt[1]))
    file.close()
