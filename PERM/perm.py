import math
from itertools import permutations 


with open("rosalind_perm.txt","r") as f:
    n=int(f.readline().strip())

print(math.factorial(n))
permuts=permutations(range(1,n+1))
for item in permuts:
    for num in item:
        print(num,end=' ')
    print('\r')