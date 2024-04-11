n=input('Ile liczb wypisac? ')
while not n.isdecimal:
    n=input('Podaj liczbe naturalna ')
n=int(n)
i=0
while i<n:
    if(i%2==0):
        print(i,end= ' ')
    i+=1
print(i)
print()
for i in range (0,n+1):
    if(i%2==0):
        print(i, end=' ')
