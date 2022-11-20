
with open('rosalind_seto.txt') as f:
    n, A, B=f.readlines()
n=int(n.strip())


setA=A.strip().rstrip('}').lstrip('{').split()
A = set([int(i.strip(',')) for i in setA])
setB=B.strip().rstrip('}').lstrip('{').split()
B = set([int(i.strip(',')) for i in setB])

union=A.union(B)
intersect=A.intersection(B)
AwoutB=A-intersect
BwoutA=B-intersect
Acompl=set([*range(1,n+1)])-A
Bcompl=set([*range(1,n+1)])-B


f = open("seto_out.txt", "w")
f.write(''.join(str(union))+'\n')
f.write(''.join(str(intersect))+'\n')
f.write(''.join(str(AwoutB))+'\n')
f.write(''.join(str(BwoutA))+'\n')
f.write(''.join(str(Acompl))+'\n')
f.write(''.join(str(Bcompl)))
f.close


