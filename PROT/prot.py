final_str=''

codon = {}
with open("codon_table.txt") as f:
    for line in f:
        key, value = line.split()
        codon[key] = value


with open("rosalind_prot.txt") as f:
    line = f.readlines()
for i in range(2,len(line[0])):
    if i%3==2:
        str=line[0][i-2]+line[0][i-1]+line[0][i]
        val=codon[str]
        if val=='Stop':
            final_str+=' '
        else:
            final_str+=val

print(final_str)