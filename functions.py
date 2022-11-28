from os import system
from data import *
fajlnev='ratingek.txt'
commentfajl='commentek.txt'
#betoltesek____________________________________________________________________________________________________________________________-
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
def menubetotes():
    valasztas=''
    while valasztas!='0':
        valasztas=menu()
        if valasztas=='1':
            system('cls')
            elsomenuponty()
        elif valasztas=='2':
            system('cls')
            masodikmenuponty()
        elif valasztas=='3':
            system('cls')
            harmadikmenuponty()
        elif valasztas=='4':
            system('cls')
            negyedikmenuponty()
        elif valasztas=='5':
            system('cls')
            otodikmenuponty()
        elif valasztas=='6':
            system('cls')
            hatodikmenuponty()
def fajlbetoltes():
    file=open(fajlnev, 'r', encoding='utf-8')
    for i in file:
        darabolt=i.strip().split(';')
        nevekratinghez.append(darabolt[0])
        ratingek.append(darabolt[1])
    file.close()
    file=open(commentfajl, 'r', encoding='utf-8')
    for i in file:
        darabolt=i.strip().split(';')
        nevekcommenthez.append(darabolt[0])
        commentek.append(darabolt[1])
    file.close()
#mentesek____________________________________________________________________________________________________________________________
def cegmentese(nev):
    file=open(fajlnev,'a',encoding='utf-8')
    file.write(f'\n{nev};')
    file=open(commentfajl,'a',encoding='utf-8')
    file.write(f'\n{nev};')
    file.close()
def ratingmentese(rating):
    file=open(fajlnev,'a',encoding='utf-8')
    for i in range(len(nevekratinghez)):
        file.write(f'{nevekratinghez[i]};{ratingek[i]}\n')
    file.close()
def commentmentese():
    file=open(commentfajl,'a',encoding='utf-8')
    for i in range(len(nevekratinghez)):
        file.write(f'{nevekratinghez[i]};{commentek[i]}\n')
    file.close()
#menupontok____________________________________________________________________________________________________________________________
def elsomenuponty():
    print('------CÉGEK------')
    for i in nevekratinghez:
        print(f'\t{i}')
    input()
def masodikmenuponty():#!!!
    for i in range(len(nevekratinghez)):
        print(f'{i+1}. {nevekratinghez[i]}')
    bekertrating=0
    choice=0
    while choice<1 or choice>len(nevekratinghez): 
        choice=int(input('melyik céghez szeretne értékelést írni?:'))
    while bekertrating<1 or bekertrating>5 and bekertrating:    
        bekertrating=int(input('mi legyen az értékelés?:'))
    ratingek[bekertrating-1]=ratingek[bekertrating-1]+','+bekertrating
    ratingmentese()
    input('sikeresen elmentettük...')
def harmadikmenuponty():
    print('-------ÚJ CÉG------')
    bekertceg=input('A cég neve: ')
    nevekratinghez.append(bekertceg)
    cegmentese(bekertceg)
    input('Sikeres felvétel.')  
def negyedikmenuponty():#!!!
    pass   
def otodikmenuponty():#!!!
    print('------CÉGEK------')
    for i in range(len(nevekratinghez)):
        print(f'{i+1}. {nevekratinghez[i]}')
    bekertcegszama= int(input('cég száma:'))
    bekertszoveg= input('szöveg:')
    nemI=0
    with open(fajlnev, 'r',encoding='UTF-8') as file:
        for i in file:
            if nemI == bekertcegszama:
                with open(commentfajl, 'a', encoding='UTF-8') as file:
                    file.write(nevekratinghez[nemI])
                    file.write(bekertszoveg)
            nemI+=1
    input('sikeresen elmentettük...')    
def hatodikmenuponty():
    i=0
    print('------CÉGEK VISSZAJELZÉSEI------')
    while i!=len(nevekcommenthez):
        print(f'\t{nevekcommenthez[i]}\t{commentek[i]}')
        i+=1
    input()