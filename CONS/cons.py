from Bio import SeqIO
import numpy as np

seqs=[]
record_dict = SeqIO.to_dict(SeqIO.parse("rosalind_cons.txt", "fasta"))
for key, value in record_dict.items():
    seqs.append(str(value.seq))

length=len(seqs[0])
profile=np.zeros((4,length)).astype('int')

for i in range(len(seqs)):
    for j in range(length):
        if seqs[i][j]=='A':
            profile[0][j]+=1
        elif seqs[i][j]=='C':
            profile[1][j]+=1
        elif seqs[i][j]=='G':
            profile[2][j]+=1
        elif seqs[i][j]=='T':
            profile[3][j]+=1

consensus=np.argmax(profile, axis=0)

final_consensus=[]
for item in consensus:
    if item==0:
        final_consensus.append('A')
    elif item==1:
        final_consensus.append('C')
    elif item==2:
        final_consensus.append('G')
    elif item==3:
        final_consensus.append('T')

for item in final_consensus:
    print(item,end='')
print('\r')
letters=['A','C','G','T']
for i in range(4):
    print(letters[i]+':',end=' ')
    for j in range(length):
        print(profile[i][j],end=' ')
    print('\r')
