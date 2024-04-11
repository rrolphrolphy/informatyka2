n=input('Podaj liczbe naturalna ')
while not n.isdecimal:
    n=input('Blad, podaj liczbe naturalna ')
n=int(n)
print('2 ^',n,'=',2**n)