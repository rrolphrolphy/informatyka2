def czynnikiN(n):
    a=[]
    i=2
    while n!=1:
        while n%i==0:
            a.append(i)
            n/=i
        if i==2:
            i+=1
        else:
            i+=2
    return a
def czynnikiN2(n):
    a=[]
    dzielnik=2
    while n>1:
        if n % dzielnik == 0:
            a.append(dzielnik)
            n/=dzielnik
        else:
            dzielnik += 1
    return a
def liczby():
    a = input('wprowadz liczbe naturalna ')
    while not a.isdecimal:
      a=input('blad, podaj naturalna liczbe ')
    return int(a)
n=liczby()
print(czynnikiN(n))
print(czynnikiN2(n))