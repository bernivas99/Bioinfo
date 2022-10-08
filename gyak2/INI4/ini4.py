def func3(a,b):
    szumma=0
    for i in range(a,b+1):
        if i%2==1:
            szumma+=i
    return szumma

print(func3(100,200))