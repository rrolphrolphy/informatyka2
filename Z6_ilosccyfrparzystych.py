n=input('Podaj liczbę naturalną trzycyfrową ')
n=int(n)
if(n<100 or n>999):
    print('Nieprawidłowa liczba')
else:
    s=0
    a=n//100
    b=n//10
    b=b%10
    c=n%10
    if(a%2==0):
        s=s+1
    if (b % 2==0):
        s=s+1
    if (c % 2==0):
        s=s+1
    print('Ilość cyfr parzystych liczby n wynosi',s)