#zad1
class Moneta:
    def __init__(self, wartosc):
        if wartosc in [1, 2, 5, 10, 20, 50, 100, 200, 500] != False:
            self.__wartosc = wartosc
        else:
            print("Nie ma takiego nominalu! Zacznynamy 1 to 1 grosz")
    def GetWartosc(self):
        return self.__wartosc
def zad1():
    jeden = Moneta(1)
    print(jeden.GetWartosc())
    niema = Moneta(7)
#zad1()

#zad2

class Skarbonka:
    def __init__(self):
        self.lista = []
    def DodajMonete(self, X):
        if isinstance(X, Moneta):
            self.lista.append(X)
        else:
            print("Przeslany obiekt nie jest moneta")
    def GetSuma(self):
        s = 0
        for i in self.lista:
            s = s + int(i.GetWartosc())
        return s
def zad2():
    jeden = Moneta(1)
    dwa = Moneta(2)
    piec = Moneta(5)

    S = Skarbonka()
    S1 = Skarbonka()

    S.DodajMonete(jeden)
    S.DodajMonete(dwa)
    S.DodajMonete(1)
    print(S.GetSuma())

    S1.DodajMonete(jeden)
    S1.DodajMonete(dwa)
    S1.DodajMonete(piec)
    print(S1.GetSuma())
#zad2()

