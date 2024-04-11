def NWD (a, b):
    while b!=0:
       a, b=b, a%b
    return a
l1=input('Podaj licznik pierwszego ulamka ')
while not l1.isdecimal():
    l1=input('Blad, podaj prawidlowa liczbe ')
l1=int(l1)
m1=input('Podaj mianownik pierwszego ulamka ')
while not m1.isdecimal() or m1=='0':
    m1=input('Blad, podaj prawidlowa liczbe ')
m1=int(m1)
l2=input('Podaj licznik drugiego ulamka ')
while not l2.isdecimal():
    l2=input('Blad, podaj prawidlowa liczbe ')
l2=int(l2)
m2=input('Podaj mianownik drugiego ulamka ')
while not m2.isdecimal() or m2=='0':
    m2=input('Blad, podaj prawidlowa liczbe ')
m2=int(m2)
licznik=l1*l2
mianownik=m1*m2
n=licznik
licznik=int(licznik/NWD(n, mianownik))
mianownik=int(mianownik/NWD(n, mianownik))
if licznik//mianownik!=0:
    c=licznik//mianownik
    licznik-=c*mianownik
    print('Wynik mnozenia to', c ,'i', licznik, '/', mianownik)
else:
    print('Wynik mnozenia to', licznik, '/', mianownik)