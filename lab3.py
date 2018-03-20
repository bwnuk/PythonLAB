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