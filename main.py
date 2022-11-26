from functions import *
from os import system
fajlbetoltes()
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
        pass