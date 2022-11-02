import numpy as np

def kmp_failure_arr(s):
    m=len(s)
    P_arr=np.zeros(m).astype('int')
    for i in range(1,m):
        k=P_arr[i-1]
        while k>0 and s[k]!=s[i]:
            k=P_arr[k-1]
        if s[k]==s[i]:
            k+=1
        P_arr[i]=k
    return P_arr 

with open('rosalind_subs_kmp.txt') as f:
    s, t = f.readlines()
    s=s.strip('\n')
    t=t.strip('\n')

n=len(s)
m=len(t)
P_arr=kmp_failure_arr(t)
q=0 
for i in range(n):
    while q>0 and t[q]!=s[i]:
        q=P_arr[q-1]
    if t[q]==s[i]:
        q+=1
    if q==m:
        print(i-m+2,end=' ') 
        q=P_arr[q-1]
    