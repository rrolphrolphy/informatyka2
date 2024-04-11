import random
n=input('Podaj liczbe naturalna')
while not n.isdecimal:
    n=input('Blad, podaj prawidlowa liczbe')
n=int(n)
a=[]
for i in range (1, n+1):
    a.append(random.randint(-100,100))
print('W liscie znajduje sie', a.count(10), 'dziesiatek')
