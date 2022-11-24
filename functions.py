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
    print('5 - cég értékelésének megtekintése')
    return input('Választás: ')

def cuccmentesefajlvegere(nev,rating):
    file=open(fajlnev,'a',encoding='utf-8')
    file.write(f'\n{nev};{rating}')

def cuccmentese():
    file=open(fajlnev,'w',encoding='utf-8')
    for i in range(len(nevek)):

        file.write(f'{nevek[i]};{ratingek[i]}\n')
    file.close()


def fajlbetoltes():
    file=open(fajlnev, 'r', encoding='utf-8')
    for row in file:
        darabolt=row.strip().split(';')
        nevek.append(darabolt[0])
        ratingek.append(darabolt[1])
    file.close()

def elsomenuponty():
    system('cls')
    print('------CÉGEK------')
    for i in nevek:
        print(f'\t{i}')
    input()

def masodikmenuponty():
    for i in range(len(nevek)):
        print(f'{i+1}. {nevek[i]}')
    choice=int(input('melyik céghez szeretne értékelést írni?:'))
    #    for i in range(len(ratingek)):
    bekertrating=input('mi legyen az értékelés?:')
    ratingek[choice-1]=ratingek[choice-1]+','+bekertrating

    
    cuccmentese()
    input('sikeresen elmentettük...')
     