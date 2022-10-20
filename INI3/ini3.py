with open('rosalind_ini3.txt') as f:
    t= f.readlines()
for item in t:
    item=item.strip()
a,b,c,d=t[1].split(' ')

def func(s,a,b,c,d):
    return s[a:b+1]+" "+s[c:d+1]

print(func(t[0],int(a),int(b),int(c),int(d)))
