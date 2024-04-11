def sumacyfr(n):
    for a in n:
        suma+=int(a)
    return suma
n=input('Podaj liczbe naturalna')
while not n.isdecimal:
    n=input('Blad, podaj prawidlowa liczbe')
