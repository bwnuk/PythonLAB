def ciag(x):
    s = 0
    s1 = 1
    for i in range(1,x):
        s1 = s1 + s
        s = s1 - s
    return s1
def rek(x):
    if x < 3:
        return 1
    else:
        return rek(x-1)+rek(x-2)