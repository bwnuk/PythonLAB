#zad1
#zad4
class Moneta:

    def __init__(self, wartosc, W):
        self.__waluta = W
        if wartosc in [1, 2, 5, 10, 20, 50, 100, 200, 500]:
            self.__wartosc = wartosc
        else:
            print("Nie ma takiego nominalu! Zacznynamy 1 to 1 grosz")
        if W in ['PLN', 'EUR', 'GP', '$']:
            self.__waluta = W
        else:
            print("Nie ma takiej dostepnej waluty")

    def GetWartosc(self):
        return self.__wartosc
    def GetWaluta(self):
        return self.__waluta

def zad1():
    jeden = Moneta(1)
    print(jeden.GetWartosc())
    niema = Moneta(7)
#zad1()

#zad3klasa
class PrzechowywaczMonet:

    def __init__(self, L):
        self.__Lista = L
        self.__monety = []

    def Dodaj(self, X):
        self.__monety.append(X)

    def Ilosc(self):
        return len(self.__monety)

    def Zwracanie(self, X):
        for x in self.__monety:
            if x.GetWartosc() == X:
                return self.__monety(x)

#zad2

class Skarbonka(PrzechowywaczMonet):
    def __init__(self, W, L):
        PrzechowywaczMonet.__init__(L)
        self.__waluta = W
        self.__lista = []

    def DodajMonete(self, X):
        if isinstance(X, Moneta):
            if X.GetWaluta() == self.__waluta:
                self.lista.append(X)
            else:
                print("Nieznana moneta")
        else:
            print("Przeslany obiekt nie jest moneta")

    def GetSuma(self):
        s = 0
        for i in self.lista:
            s = s + int(i.GetWartosc())
        return s

    def Zwracanie(self, X):
        if self.Ilosc() < 2:
            print("Nie mozna wyciagnac pojedyneczej monety")

def zad2():
    jeden = Moneta(1, "PLN")
    dwa = Moneta(2, "PLN")
    piec = Moneta(5, "EURO")

    S = Skarbonka("PLN")
    S1 = Skarbonka("PLN")

    S.DodajMonete(jeden)
    S.DodajMonete(dwa)
    S.DodajMonete(1)
    print(S.GetSuma())

    S1.DodajMonete(jeden)
    S1.DodajMonete(dwa)
    S1.DodajMonete(piec)
    print(S1.GetSuma())
zad2()

#zad3
def zad3():
    P = PrzechowywaczMonet([1, 2, 5, 10, 20, 50, 100, 200, 500])
    jeden = Moneta(1)
    dwa = Moneta(2)
    piec = Moneta(5)

    P.Dodaj(jeden)
    print(P.Ilosc())
    P.Dodaj(dwa)
    P.Dodaj(piec)
    print(P.Ilosc())

    print(P.Zwracanie(1).GetWartosc())

#zad3()