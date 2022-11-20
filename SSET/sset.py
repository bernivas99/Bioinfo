with open('rosalind_sset.txt') as f:
    n=int(f.readline().strip())

mod=1000000
outp=pow(2,n)%mod
print(outp)