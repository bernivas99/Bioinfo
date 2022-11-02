from Bio import SeqIO
import numpy as np

def kmp_failure_arr(s):
    m=len(s)
    P_arr=np.zeros(m).astype('int')
    for q in range(1,m):
        k=P_arr[q-1]
        while k>0 and s[k]!=s[q]:
            k=P_arr[k-1]
        if s[k]==s[q]:
            k+=1
        P_arr[q]=k
    return P_arr 



record_dict = SeqIO.to_dict(SeqIO.parse("rosalind_kmp.txt", "fasta"))
for key, value in record_dict.items():
    s=str(value.seq)

P_arr=kmp_failure_arr(s)
with open("result.txt", "w") as f:
    f.write(' '.join(P_arr.astype('str')))




