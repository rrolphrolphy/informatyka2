import math
def liczby():
    a = input('wprowadz liczbe naturalna ')
    while not a.isdecimal:
      a=input('blad, podaj naturalna liczbe ')
    return int(a)
def pierwszaN(n):
    if n==0 or n==1:
        return False
    for i in range (2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
n=liczby()
if pierwszaN(n):
    print('liczba jest liczba pierwsza')
else:
    print('liczba nie jest liczba pierwsza')