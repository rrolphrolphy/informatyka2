def dzielenie(a, b):
    return a%b==0
a=input('podaj liczbe naturalna dodatnia ')
while not a.isdecimal():
    a=input('blad, podaj prawidlowa liczbe ')
a=int(a)
wynik = 0
for i in range (1, a+1):
    if dzielenie(a, i):
        wynik+=1
print('liczba ma', wynik, 'dzielnikow')
