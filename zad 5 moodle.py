def dzielenie3(a):
    return a%3==0
a=input('podaj liczbe naturalna dodatnia ')
while not a.isdecimal():
    a=input('blad, podaj prawidlowa liczbe ')
a=int(a)
wynik = 0
for i in range (1, a+1):
    if dzielenie3(i):
        wynik+=1
print('w zakresie jest', wynik, 'liczb podzielnych przez 3')

