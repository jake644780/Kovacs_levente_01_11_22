from os import system
from data import *
fajlnev='cégek.txt'

def menu():
    system('cls')
    print('------MENÜ------')
    print('0 - kilépés')
    print('1 - cégek kilistázása')
    print('2 - új rating')
    print('3 - új cég')
    print('4 - rating törlése')
    return input('Választás: ')


def fajlbetoltes():
    file=open(fajlnev, 'r', encoding='utf-8')
    for row in file:
        darabolt=row.strip().split(';')
        nevek.append(darabolt[0])
        ratingek.append(float(darabolt[1]))
    file.close()

def elsomenuponty():
    system('cls')
    print('------CÉGEK------')
    for i in nevek:
        print(f'\t{i}')
    input()
