"""DOKUMENTACJA
"""
srodek = int(92)
def lewo(S):
    print(S)
def prawo(S):
    x = (srodek*2) - len(S)-1
    print(" "*x, S)
def srodkowanie(S):
    x = srodek - len(S)
    print(" "*x, S)