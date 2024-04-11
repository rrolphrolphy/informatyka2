a=input('Podaj liczbę naturalną trzycyfrową ')
a=int(a)
if(a<100 or a>999):
    print('Nieprawidłowa liczba')
else:
    s=a//100
    if(s%2==0):
        print('Pierwsza cyfra liczby a jest parzysta')
    else:
        print('Pierwsza cyfra liczby a jest nieparzysta')