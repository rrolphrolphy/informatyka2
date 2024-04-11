n=input('Podaj liczbę naturalną czterocyfrową ')
while not n.isdecimal():
    n=input('Liczba nie jest naturalna, podaj liczbe naturalną czterocyfrową ')
n=int(n)
if(999<n<10000):
    a=n//1000
    b=(n%1000)//100
    c=(n%100)//10
    d=n%10
    if(a<b):
        a=b
    if (a < c):
        a = c
    if (a < d):
        a = d
    print('Najwieksza cyfra liczby jest', a)
else:
    print("Nieprawidłowa liczba")
