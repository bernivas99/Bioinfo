with open('rosalind_ini2.txt') as f:
    t1, t2 = f.readlines()[0].strip().split(' ')

print(int(t1)**2+int(t2)**2)