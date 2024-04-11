import random
#n=input('Podaj liczbę ')
#while not n.isdecimal:
#    n=input('Blad. Podaj liczbe naturalna ')
#n=int(n)
n=int(random.random()*1000000)
liczba=n
cyfra=1
suma=0
while n!=0:
    cyfra=n%10
    suma+=cyfra
    n=n//10
print('Suma cyfr liczby', liczba ,' wynosi ', suma)