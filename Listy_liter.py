# def spacja(n):
#     if n.count(' ')>0:
#         return n.index(' ')
#     else:
#         return 'nie ma spacji'
# def samogloski(n):
#     sam='aeiouy'
#     wynik = 0
#     for i in n:
#         if i.lower() in sam:
#             wynik+=1
#     return wynik
# n=input('Podaj dowolny ciąg znaków ')
# a=input('Ktorego znaku szukasz ')
# print('Znak znajduje sie w tekscie?', n.lower().count(a)>0)
# print('Ilośc liter', a, 'to', n.lower().count(a))
# print('Miejsce spacji w tekście to:', spacja(n))
# print('Ilosc samoglosek w tekscie to:', samogloski(n))
def czyparzysta(b):
    return b[-1]=='0'
b=input('Podaj liczbe binarna')
print('Liczba jest parzysta:', czyparzysta(b))