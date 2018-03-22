import math
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
    L =  []
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
            s =s+ int(S[w][ww])
        s = s/3
        if s < 3:
            print(w, S[w])
def f_2(S, x):
    s = 0
    for w in S.keys():
        for ww in S[w].keys():
            if ww != x:
                print("RAZ")
def zad5():
    #f({'Mietek': {'python': 1, 'odpowiedz ustna': 2, 'lisp': 3}, 'Mirek': {'python': 2, 'odpowiedz ustna': 2, 'lisp': 3},'Marek': {'python': 4, 'odpowiedz ustna': 3, 'lisp': 3}})
    f_2({'Mietek': {'python': 1, 'odpowiedz ustna': 2, 'lisp': 3}, 'Mirek': {'python': 2, 'odpowiedz ustna': 2, 'lisp': 3},'Marek': {'python': 4, 'odpowiedz ustna': 3, 'lisp': 3}}, 'lisp')
#zad5()