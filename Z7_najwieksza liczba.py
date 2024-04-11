a=input('Podaj pierwszą liczbę rzeczywistą ')
b=input('Podaj drugą liczbę rzeczywistą ')
c=input('Podaj trzecią liczbę rzeczywistą ')
a=float(a)
b=float(b)
c=float(c)
maks=a
if(b>maks):
    maks=b
if(c>maks):
    maks=c
print('Największą liczbą jest',maks)