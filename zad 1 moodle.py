def pitagoras (a,b,c):
    liczby=[a,b,c]
    liczby.sort()
    return liczby[0]*liczby[0]+liczby[1]*liczby[1]==liczby[2]*liczby[2]
def liczby ():
    a = input('podaj liczbe naturalna dodatnia ')
    while not a.isdecimal or a=='0':
      a=input('blad, podaj poprawna liczbe ')
    return int(a)
if pitagoras(liczby(), liczby(), liczby()):
    print('liczby sa pitagorejskie')
else:
    print('liczby nie sa pitagorejskie')