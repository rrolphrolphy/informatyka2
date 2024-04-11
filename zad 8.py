def wynik(n):
    silnia=1
    suma=1
    for i in range (2, n+1):
        silnia*=i
        suma+=i
    return float(suma/silnia)
a=input('podaj liczbe naturalna dodatnia ')
while not a.isdecimal():
    a=input('blad, podaj prawidlowa liczbe ')
a=int(a)
print(wynik(a))
