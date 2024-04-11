def liczby():
    a = input('wprowadz liczbe naturalna')
    while not a.isdecimal:
      a=input('blad, podaj naturalna liczbe ')
    return int(a)
def dzielnikiN(n):
    a=[]
    for i in range (1,n+1):
        if n%i==0:
            a.append(i)
    return a
n=liczby()
print(dzielnikiN(n))

