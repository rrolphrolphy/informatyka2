a=int(input('Wprowadz liczbe naturalna trzycyfrowa a'))
if 100>a or a>999:
    print('a nie jest liczba trzycyfrowa')
else:
    s=a//100
    if s%2==0:
        print('Pierwsza cyfra liczby a jest parzysta')
    else:
        print('Pierwsza cyfra liczby a nie jest parzysta')


