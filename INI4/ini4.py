def func(a,b):
    szumma=0
    for i in range(a,b+1):
        if i%2==1:
            szumma+=i
    return szumma


with open('rosalind_ini4.txt') as f:
    t1, t2 = f.readlines()[0].strip().split(' ')
print(func(int(t1),int(t2)))