a=input('Podaj liczbe naturalna ')
while not a.isdecimal:
    a=input('Blad, podaj liczbe naturalna ')
a=int(a)
b=input('Podaj liczbe naturalna ')
while not b.isdecimal:
    b=input('Blad, podaj liczbe naturalna ')
b=int(b)
while a==0 and b==0:
    b=input('Obie liczby nie moga byc zerem, podaj druga liczbe ponownie ')
    while not b.isdecimal:
        b = input('Blad, podaj liczbe naturalna ')
    b=int(b)
if a==0:
    print(b)
elif b==0:
    print(a)
else:
    c=a
    d=b
    while not b==0:
        if a>b:
            a=a-b
        else:
            b=b-a

    print(a)
print(c*d//a)
