import math
import time
import random
#zad1
def sincos(x):
    a = math.sin(math.radians(x)), math.cos(math.radians(x))
    return a
def zad1():
    for i in range(0, 99, 9):
        b = sincos(i)
        print("Kat: ", i, "; sin: ", b[0], "; cos: ", b[1])
#zad1()

#zad2
def f_2(x,y):
    return (y, y+x)
def zad2():
    w = int(input("Podaj wyraz ciagu: "))
    b = f_2(0, 1)
    for i in range(2, w, 1):
        b = f_2(*b)
    print(b[1])
#zad2()

#ZAD3
def f_3(L, K):
    LW = [(L[i-1]*K[0]+L[i]*K[1]+L[i+1]*K[2])/3 if i != 0 and i <(len(L)-1) else L[i] for i in range(len(L)) ]
    return LW

def zad3():
    print(f_3([3,1,2,0,4], (1, 1, 1)))
    print(f_3([3, 1, 2, 0, 4], (2, -1, 2)))
#zad3()

#ZAD4
def f_al(S):
    L = []
    for w in S.keys():
        L.append(w)
    L.sort()
    return L
def f_L(S):
    for w in S.keys():
        print(w, S[w])
def zad4():
    print(f_al({'ALA': 4, 'Andrzej': 5, 'XD': 1}))
#zad4()

#zad5
def f(S):
    for w in S.keys():
        s = 0
        for ww in S[w].keys():
            s = s + int(S[w][ww])
        s = s/3
        if s < 3:
            print(w, S[w])
def f_2(S, x):
    s = 0
    i = 0
    for w in S.keys():
        for ww in S[w].keys():
            if ww == x:
                s = s + int(S[w][ww])
                i = i + 1
    s = s / i
    print(s)
def zad5():
    f({'Mietek': {'python': 1, 'odpowiedz ustna': 2, 'lisp': 3}, 'Mirek': {'python': 2, 'odpowiedz ustna': 2, 'lisp': 3},'Marek': {'python': 4, 'odpowiedz ustna': 3, 'lisp': 3}})
    f_2({'Mietek': {'python': 1, 'odpowiedz ustna': 2, 'lisp': 3}, 'Mirek': {'python': 2, 'odpowiedz ustna': 2, 'lisp': 3},'Marek': {'python': 4, 'odpowiedz ustna': 3, 'lisp': 3}}, 'lisp')
#zad5()

#zad6
def f(S):
    W = {}
    for w in S.keys():
        if int(S[w]) > 200:
            W[w] = 'Sen wieczny'
        elif int(S[w])>0:
            W[w] = (8/math.log10(int(S[w])))
    return W
#def f_2(S):
    #niedziala
    #w = {' '+key: (8/math.log10(S[key]) if S[key]<=200 else 'Sen wieczny' for key in S.keys() if S[key]>0}
def zad6():
    print(f({'Mietek': 23, 'Marcin': 12, 'Zombie': 201, 'Zbyszek': 88}))
#zad6()

#zad7
def T_OR_F():
    if random.randint(1, 2)  == 2:
        return True
    else:
        return False
def Wypelnianie(T):
    for i in range(0, 20):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        while T[x][y] == True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        T[x][y] = T_OR_F()
def Strzelanie(Tab):
    counter = 20
    x = int(input("Podaj x: "))
    y = int(input("Podaj y: "))
    k = x, y
    T = {k}
    Set = {k}
    if Tab[x][y] == True:
        counter = counter - 1
        print("Trafiony")
    else:
        print("Pudlo")
    while counter >0:
        x = int(input("Podaj x: "))
        y = int(input("Podaj y: "))
        k = x, y
        T = {k}
        if Set.issubset(T) == False:
            if Tab[x][y] == True:
                counter = counter - 1
                print("Trafiony")
            else:
                print("Pudlo")

            Set.add(k)
        else:
            print("Juz tam strzelano")


def zad7():
    Tabela = [[False for i in range(10)]for j in range(10)]
    for i in range(10):
        print(Tabela[i])
    Wypelnianie(Tabela)
    print("")
    for i in range(10):
        print(Tabela[i])
    Strzelanie(Tabela)
#zad7()
for x, y in [[0.0,0.0],[-0.5,0.9],[1.4,-1.4]]:
    print(x, y)
