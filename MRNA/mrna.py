
codon={}
with open("codon_table.txt") as f:
    for line in f:
        key, value = line.split()
        codon[key] = value

with open('rosalind_mrna.txt') as f:
    protein=f.readline().strip()

modulo=1000000
product=1
for char in protein:
    char_cnt=len({item for item in codon if codon[item]==char})
    product*=char_cnt
    product=product%modulo

product*=3  #because of stop codon
product=product%modulo

print(product)
