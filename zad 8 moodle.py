import random
def liczby ():
    a = input('ile liczb losowac ')
    while not a.isdecimal or a=='0':
      a=input('blad, podaj naturalna liczbe ')
    return int(a)
def najwieksza(n):
    naj=0
    for i in range(n):
        a=random.randint(0, 100)
        print(a, end = ' ')
        if a>naj:
            naj=a
    return naj
def najwieksza1(n):
    naj=0
    a=[]
    for i in range (n):
        a.append(random.randint(0, 100))
    print(a)
    return max(a)
n=liczby()
print('najwieksza liczba to', najwieksza(n))
print('najwieksza liczba to', najwieksza1(n))