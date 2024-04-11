def pitagoras (a,b,c):
    liczby=[a,b,c]
    liczby.sort()
    return liczby[0]*liczby[0]+liczby[1]*liczby[1]==liczby[2]*liczby[2]
for i in range (1,11):
    for j in range (i,11):
        for k in range (j,11):
            if pitagoras(i,j,k):
                print(i,j,k)