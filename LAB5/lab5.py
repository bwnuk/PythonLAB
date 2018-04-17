import text
import random
#ZAD 1
def zad1():
    print("ZAD 1")
    text.lewo("MACIEK: ELO ELO")
    text.prawo("JA: DADADADA ANACONDA")
    text.srodkowanie("11.01.2011 19:16")
zad1()
#ZAD 2
#WYWOLAC OSOBNO text2

#ZAD 3
def zad3():
    print("ZAD 3")
#zad3()

#ZAD4
def zad4():
    print("ZAD 4")
    akto=[]
    acozrobil=[]
    ajaki=[]
    aco=[]

    with open('01_kto.txt', 'r') as k:
        for line in k:
            akto.append(line)
    with open('02_co_zrobil.txt', 'r') as k1:
        for line in k1:
            acozrobil.append(line)
    with open('03_jaki.txt', 'r') as k2:
        for line in k2:
            ajaki.append(line)
    with open('04_co.txt', 'r') as k3:
        for line in k3:
            aco.append(line)
    print("{kto} {co_zrobil} {jaki} {co}".format(
        kto=random.choice(akto),
        co_zrobil=random.choice(acozrobil),
        jaki=random.choice(ajaki),
        co=random.choice(aco),
    ))
    with open('wynik.txt', 'w') as w:
        for i in range(100):
            w.write("{kto} {co_zrobil} {jaki} {co}".format(
            kto=random.choice(akto),
            co_zrobil=random.choice(acozrobil),
            jaki=random.choice(ajaki),
            co=random.choice(aco),
            ))
zad4()