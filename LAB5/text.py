"""DOKUMENTACJA
"""
def lewo(S, liczba=200):
    print(S.ljust(liczba))
def prawo(S, liczba=200):
    print(S.rjust(liczba))
def srodkowanie(S, liczba=200):
    print(S.center(liczba))

if __name__ == "__main__":
    import struct
    print('Moduł "text" definiuje funkcje do_lewej, do_prawej, do_srodka i służy do:')
    lewo("Tekst wyrównany do lewej")
    prawo("Tekst wyrownany do prawej")
    srodkowanie("Tekst wycentrowany")
    print("Dodatkowo, moduł zawiera:", end='')
    print(dir(struct))
    print(dir(__name__))