from Bio import SeqIO
from kmer_utils import kmp, generate_all_combos


combi=generate_all_combos('ACTG',4)

words=[]
for word in combi:
    words.append("".join(word))
words.sort()

record_list = list(SeqIO.parse("rosalind_kmer.txt", "fasta"))
s=record_list[0].seq

counts=[]
for word in words:
    cnt=kmp(s,word)
    counts.append(cnt)

for cnt in counts:
    print(cnt,end=' ')
