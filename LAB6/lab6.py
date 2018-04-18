#zad1
class Moneta:
    def __init__(self, wartosc):
        if wartosc in [1, 2, 5, 10, 20, 50, 100, 200, 500] != False:
            self.__wartosc = wartosc
        else:
            print("Nie ma takiego nominalu! Zacznynamy 1 to 1 grosz")
    def GetWartosc(self):
        return self.__wartosc

jeden = Moneta(1)
print(jeden.GetWartosc())
niema = Moneta(7)