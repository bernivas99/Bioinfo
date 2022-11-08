from Bio import SeqIO

record_list = list(SeqIO.parse("rosalind_splc.txt", "fasta"))
s=record_list[0].seq
for i in range(1,len(record_list)):
    s=s.replace(record_list[i].seq,"")
s=s.replace("T","U")


codon = {}
with open("codon_table.txt") as f:
    for line in f:
        key, value = line.split()
        codon[key] = value

final_str=''
for i in range(2,len(s)):
    if i%3==2:
        str=s[i-2]+s[i-1]+s[i]
        val=codon[str]
        if val=='Stop':
            final_str+=' '
        else:
            final_str+=val

print(final_str)
    
