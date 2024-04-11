n=input('Podaj liczbe naturalna dodatnia ')
while not n.isdecimal() or n==0:
    n=input('Blad, podaj liczbe naturalna dodatnia ')
n=int(n)
silnia=1
suma=1
for i in range(2,n+1):
    silnia=silnia*i
    suma=suma+i
wynik=suma/silnia
print('Wynik dzialania to', wynik)

