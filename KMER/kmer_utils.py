import numpy as np
from itertools import combinations_with_replacement,permutations

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

def kmp(s,t):
    cnt=0
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
            cnt+=1
            q=P_arr[q-1]
    return cnt


def generate_all_combos(alphabet,n):
    all_combos=[]
    combi_list=list(combinations_with_replacement(alphabet,n))
    for item in combi_list:
        perm=permutations(item)
        all_combos=all_combos+list(perm)
    combi=set(all_combos)
    return combi