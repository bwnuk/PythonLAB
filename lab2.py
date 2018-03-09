import math
import random
import time

#start zad 1
def liczby_pierwsze(*args) ->bool:
    for i in range(len(args)):
        liczba=args[i]
        for k in range(2, liczba//2):
            if(liczba % k == 0):
                return False
        else:
            return True

def Mersenna(n):
    return (2**n) - 1

def zad1():
    tab=[31*[None]]
    for x in range(1,31):
        print(x, liczby_pierwsze(Mersenna(x)))
        #tab[x-1]=Mersenna(x)
    #for x in range(1, 31):
     #   print(x, liczby_pierwsze(tab))

#zad1()

#start zad 2
def printCenter(tekst, dl=80):
    for i in range((dl//2)-len(tekst)//2):
        print(" ", end="")
    else:
        print(tekst)

def zad2():
    printCenter("ALA MA PSA")

#zad2()

#start zad 3

def f_default(n):
    return lambda x: x+n

def funkcja(fx, xp=-1, lp=10, xk=1):
    for i in range(xp*lp, xk*lp):
        print(i/lp, fx(i/lp))

def zad3():
    funkcja(lambda x: math.cos(x))
#zad3()

#start zad 4
def k4():
    return random.randint(1, 4)

def k8():
    return random.randint(1, 8)

def k10():
    return  random.randint(1, 10)

def k20():
    return random.randint(1, 20)

def getDice(tekst):
    if (tekst == 'k4'):
        return lambda  :k4()
    elif(tekst == 'k8'):
        return  lambda : k8()
    elif(tekst == 'k10'):
        return lambda : k10()
    elif(tekst == 'k20'):
        return lambda  : k20()
    else:
        print("Bledny tekst")

def rollDice(text):
    if(len(text)>4):
        print("ZLY TEKST")
    else:
        s=0
        for i in range(int(text[0])):
            f = getDice(text[1:])
            s=s+f()
        print(s)

def zad4():
    rollDice("2k4")
    rollDice("4k10")

#zad4()

#start zad 5
def credits(*args):
    for i in range(len(args)):
        printCenter(args[i])
        time.sleep(1)


def zad5():
    credits("raz", "ra", "r")
zad5()