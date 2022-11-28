from os import system
from data import *
fajlnev='ratingek.txt'
commentfajl='commentek.txt'
def menu():
    system('cls')
    print('------MENÜ------')
    print('0 - kilépés')
    print('1 - cégek kilistázása')
    print('2 - új rating')
    print('3 - új cég')
    print('4 - cég értékelésének megtekintése')
    print('5 - visszajelzés írása')
    print('6 - visszajelzések megtekintése')
    return input('Választás: ')

def mindenmentese(nev,rating):
    file=open(fajlnev,'a',encoding='utf-8')
    file.write(f'\n{nev};{rating}')
    file.close()
def cegmentese(nev):
    file=open(fajlnev,'a',encoding='utf-8')
    file.write(f'\n{nev};')
    file=open(commentfajl,'a',encoding='utf-8')
    file.write(f'\n{nev};')
    file.close()
def ratingmentese(rating):
    file=open(fajlnev,'a',encoding='utf-8')
    for i in range(len(nevek)):
        file.write(f'{nevek[i]};{ratingek[i]}\n')
    file.close()
def commentmentese(rating):
    file=open(commentfajl,'a',encoding='utf-8')
    for i in range(len(nevek)):
        file.write(f'{nevek[i]};{commentek[i]}\n')
    file.close()

def fajlbetoltes():
    file=open(fajlnev, 'r', encoding='utf-8')
    for i in file:
        darabolt=i.strip().split(';')
        nevek.append(darabolt[0])
        ratingek.append(darabolt[1])
    file.close()
def commentbetoltes():
    file=open(commentfajl, 'r', encoding='utf-8')
    for i in file:
        darabolt=i.strip().split(';')
        nevekcommenthez.append(darabolt[0])
        commentek.append(darabolt[1])
    file.close()

def elsomenuponty():
    print('------CÉGEK------')
    for i in nevek:
        print(f'\t{i}')
    input()
def masodikmenuponty():
    for i in range(len(nevek)):
        print(f'{i+1}. {nevek[i]}')
    bekertrating=0
    choice=0
    while choice<1 or choice>len(nevek): 
        choice=int(input('melyik céghez szeretne értékelést írni?:'))
    while bekertrating<1 or bekertrating>5 and bekertrating:    
        bekertrating=str(input('mi legyen az értékelés?:'))
    ratingek[bekertrating-1]=ratingek[bekertrating-1]+','+bekertrating
    ratingmentese()
    input('sikeresen elmentettük...')
def harmadikmenuponty():
    print('-------ÚJ CÉG------')
    bekertceg=input('A cég neve: ')
    nevek.append(bekertceg)
    cegmentese(bekertceg)
    input('Sikeres felvétel.')  
def negyedikmenuponty():#!!!
    pass
def otodikmenuponty():#!!!
    print('------CÉGEK------')
    for i in range(len(nevek)):
        print(f'{i+1}. {nevek[i]}')
    bekertcegszama= int(input('cég száma:'))
    bekertszoveg= input('szöveg:')
    nemI=0
    with open(fajlnev, 'r',encoding='UTF-8') as file:
        for i in file:
            if nemI == bekertcegszama:
                with open(commentfajl, 'a', encoding='UTF-8') as file:
                    file.write(nevek[nemI])
                    file.write(bekertszoveg)
            nemI+=1
    input('sikeresen elmentettük...')       
def hatodikmenuponty():
    i=0
    print('------CÉGEK VISSZAJELZÉSEI------')
    while i != len(nevekcommenthez):
        print(f'\t{nevekcommenthez[i]}\t{commentek[i]}')
        i += 1
    input()