import math


def zad1():
    print("roznica - //")
    print(17 // 3)
    print("kwadrat - **")
    print(4 ** 4)
    print("pierwiastek")
    print(math.sqrt(4))


def zad2():
    print("~~~~~~~~ZADANIE 2~~~~~~")

    x = int(input("Wpisz rok: "))
    if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0):
        print(str(x) + " rok jest przestepny")
    else:
        print(str(x) + " rok nie jest przestepny")


# zad2()

def zad3():
    print("~~~~~~~~ZADANIE 3~~~~~~")

    for w in range(-10, 11, 1):
        print("{0:8.2f} {1:+10.6f} {1:12.2e}".format(w / 10, math.sin(w / 10)))
    # zad3()


def zad4():
    l = int(input("Wpisz liczbe: "))
    for i in range(1, int(l / 2)):
        if l % i == 0:
            print(str(l) + " liczba nie jest liczba pierwsza")
            break
    else:
        print(str(l) + " liczba jest liczba pierwsza")


# zad4()

def zad5():
    tekst = input("Wpisz tekst: ")
    for w in range(len(tekst)):
        if tekst[w] == 'a' or tekst[w] == 'ą' or tekst[w] == 'e' or tekst[w] == 'ę' or tekst[w] == 'i' or tekst[
            w] == 'o' or tekst[w] == 'ó' or tekst[w] == 'u' or tekst[w] == 'y' or tekst[w] == 'A' or tekst[w] == 'Ą' or \
                tekst[w] == 'E' or tekst[w] == 'I' or tekst[w] == 'E' or tekst[w] == 'Ę' or tekst[w] == 'O' or tekst[
            w] == 'U' or tekst[w] == 'Ó' or tekst[w] == 'Y':
            tekst = tekst[0:w] + "a" + tekst[w + 1:len(tekst)]
    print(tekst)


# zad5()

def zad5b():
    tekst = input("Wpisz tekst: ")
    for w in range(len(tekst)):
        if tekst[w] == 'a' or tekst[w] == 'ą' or tekst[w] == 'e' or tekst[w] == 'ę' or tekst[w] == 'i' or tekst[
            w] == 'o' or tekst[w] == 'ó' or tekst[w] == 'u' or tekst[w] == 'y' or tekst[w] == 'A' or tekst[w] == 'Ą' or \
                tekst[w] == 'E' or tekst[w] == 'I' or tekst[w] == 'E' or tekst[w] == 'Ę' or tekst[w] == 'O' or tekst[
            w] == 'U' or tekst[w] == 'Ó' or tekst[w] == 'Y':
            tekst = tekst[0:w] + "a" + tekst[w + 1:]
    print(tekst)


# zad5b()

def zad5c():
    tekst = input("Wpisz tekst ")
    for x in ['e', 'o', 'i', 'y', 'u']:
        tekst = tekst.replace(x, 'a')
    print(tekst)


zad5c()


def zad6():
    i = 0
    while i < 2:
        tekst = input("Wypisz dzien tygodnia: ")
        if tekst == "poniedzialek" or tekst == "poniedziałek":
            print("Najgorszy dzien")
            break
        elif tekst == "wtorek":
            print("MEH")
            break
        elif tekst == "sroda" or tekst == "środa":
            print("Coraz lepiej")
            break
        elif tekst == "czwartek":
            print("WOLNE")
            break
        elif tekst == "piątek" or tekst == "piatek":
            print("JEJ")
            break
        elif tekst == "sobota":
            print("SUPRE")
            break
        elif tekst == "niedziela":
            print("Koniec wolnego")
            break
        else:
            print("Nie podano dnia tygodnia")
            i += 1
    else:
        print("Nie ladnie tak")

# zad6()

