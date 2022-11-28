from functions import *
from os import system
#after succesful input, doesn't clear previous menupoints and stuff 
#4. menupoint does not work, have no idea what to do with it
#idea is:
#choose cég and have it's row's [1] part converted from str into int and then just szum/len
#5. menupoint problem: cannot add comment to txt due to something
commentbetoltes()
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
        system('cls')
        negyedikmenuponty()
    elif valasztas=='5':
        system('cls')
        otodikmenuponty()
    elif valasztas=='6':
        system('cls')
        hatodikmenuponty()