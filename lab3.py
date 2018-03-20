#zad 1
def f_1(L):
    max = 0
    min = L[0]
    s = 0
    for x in L:
        if x >max:
            max = x
        if x < min:
            min = x
        s = s + x
    s = s/len(L)
    print("MAX: ", max)
    print("MIN: ", min)
    print("SREDNIA: ", s)
def zad1():
    f_1([1,2,3,4,65])
#zad1()

#zad2
def f_2(L):
    NL = [x for x in L]
    return NL
def zad2():
    print(f_2([1,2,3,4,5]))
#zad2()

#zad3
def f_3(L):
    w = [(L[x]+L[x-1]+L[x+1])/3 if x!=0 and x <len(L)-1 else L[x] for x in range(len(L))]
    return w
def zad3():
    print(f_3([3,1,2,0,4]))
#zad3()

#zad 4
def f_4(a, b):
    m = 0
    w = [a[x]+ b[x]  for x in range( min(len(a), len(b)) )]
    return w

def zad4():
    print(f_4([1,2,3,4, 5, 6, 7, 8], [1,2,3,4, 5]))
#zad4()

#zad 5
def f_5(L0, L1):
    W = [L0[x]/L1[x] for x in range(min(len(L0), len(L1)))]
    return W
def zad5():
    print(f_5([1,2,3,4,5], [1,2,3,4]))
#zad5()

#zad6
def f_6(L0):
    L0.sort()
    print(L0)
    W = L0[:3]+L0[-3:]
    return W
def zad6():
    print(f_6([1,25,6,71,21,33,44,0, -1]))
#zad6()

#zad7
def f_7(L0):
    L0 = [L0[x] for x in range(len(L0)) if x % 3 == 0 or L0[x]<0]
    return L0

def f_7_d(W1):
    c = len(W1) - 1
    while c!= 0:
        if c % 3 == 0 or W1[c]<0:
            del(W1[c])
        c = c -1
    return W1

def zad7():
    print(f_7([-2, 2,4, 5, 6, 7, 8,-1, -1,-1, 22, 33 , 44, -1, 1]))
    print(f_7_d([-2, 2, 4, 5, 6, 7, 8, -1, -1, -1, 22, 33, 44, -1, 1]))
#zad7()

#zad8
def f_8(L0, o):
    a = [0]
    W = L0
    i = 0
    k = len(W)-1

    while i <= k:
        if (i+1) % (o+1) == 0:
            W = W[:i]+a+W[i:]
            k = k + 1
        i = i + 1
    return W

def zad8():
    print([1,2,3,4,5,6])
    print(f_8([1, 2, 3, 4, 5, 6, 9 , 9, 9], 3))

#zad8()

#zad9
def f_9(x):
    W = [[0 if (i-k) % 2 == 0 else 1 for i in range(x)]for k in range(x)]
    return W
def zad9():
    print(f_9(4))
zad9()