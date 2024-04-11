import random
def zamiana1(a):
    b=a
    if len(b) % 2 == 1:
        c = b.pop(-1)
        b[0::2], b[1::2] = b[1::2], b[0::2]
        b.append(c)
    else:
        b[0::2], b[1::2] = b[1::2], b[0::2]
    return b
def zamiana2(a):
    b=a
    b[0], b[-1] = b[-1], b[0]
    b[1], b[-2] = b[-2], b[1]
    return b
def srednia(a):
    b=a
    suma=0
    for i in range(0, len(a)):
        suma+=a[i]
    return suma/len(a)
n=input('Podaj liczbe naturalna wieksza od 3')
while not n.isdecimal or float(n)<4:
    n=input('Blad, podaj prawidlowa liczbe')
n=int(n)
a=[]
for i in range (1, n+1):
    a.append(random.randint(-10,50))
print(a)
print('zad.2:', zamiana1(a))
print('zad.5:', zamiana2(a))
print('zad.6:', max(a))
print('zad.7:', srednia(a))
