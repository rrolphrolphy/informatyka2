a=input('Podaj liczbę naturalną dwucyfrową ')
a=int(a)
if(a<10 or a>99):
    print('Nieprawidłowa liczba')
else:
    b=a//10
    c=a%10
    d=b+c
    print('Suma cyfr liczby dwucyfrowej wynosi', d)