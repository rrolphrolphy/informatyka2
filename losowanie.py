import random

#n=input("Ile liczb wylosowac? ")
#while not n.isdecimal():
#    n=input('Blad. Podaj liczbe naturalna')
#n=int(n)
#a=[]
#for i in range (n):
#    a.append*(random.randint(1,6))
#print(a)
#print('Piata wylosowana liczba to ', a[4])
#toto_lotek
#t=[]
#while len(t)<50:
#    p=random.randint(1, 49)
#    if p not in t:
#        t.append(p)
#print(t)
l=random.randint(1,100)
n=0
s=0
while(n!=l):
    n=input('Podaj liczbe naturalna ')
    while not n.isdecimal():
        n=input('Blad,podaj liczbe naturalna ')
    n=int(n)
    if(n>l):
        print('Podana liczba jest za duza')
    if(n<l):
        print("Podana liczba jest za mala")
    s+=1
print("Gratulacje uzytkowniku! Wygrales nowego iPhone'a!")
print("Zgadnięcie liczby zajelo ci", s, "prób/y")
