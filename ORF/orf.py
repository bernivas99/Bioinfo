from Bio import SeqIO

codon={}
with open("codon_table.txt") as f:
    for line in f:
        key, value = line.split()
        codon[key] = value


record_dict = SeqIO.to_dict(SeqIO.parse("rosalind_orf.txt", "fasta"))
for key, value in record_dict.items():
    rev_compl=value.reverse_complement()
    good_idcs,good_idcs_revcompl=[],[]
    for i in range(len(value.seq)-3):
        if value.seq[i:i+3]=='ATG':
            good_idcs.append(i)
    for i in range(len(rev_compl.seq)-3):
        if rev_compl.seq[i:i+3]=='ATG':
            good_idcs_revcompl.append(i)
    
    good_strs=[]
    for ind in good_idcs:
        for j in range(ind,len(value.seq)-3,3 ):
            if value.seq[j:j+3]=='TAA' or value.seq[j:j+3]=='TAG' or value.seq[j:j+3]=='TGA':
                good_strs.append(value.seq[ind:j+3])
                break
    for ind in good_idcs_revcompl:
        for j in range(ind,len(rev_compl.seq)-3,3 ):
            if rev_compl.seq[j:j+3]=='TAA' or rev_compl.seq[j:j+3]=='TAG' or rev_compl.seq[j:j+3]=='TGA':
                good_strs.append(rev_compl.seq[ind:j+3])
                break

    proteins=[]                
    for item in good_strs:
        final_str=''
        for i in range(2,len(item)):
            if i%3==2:
                str=item[i-2]+item[i-1]+item[i]
                val=codon[str.replace("T","U")]
                if val=='Stop':
                    final_str+=' '
                else:
                    final_str+=val
        proteins.append(final_str)
        
    proteins_set = set()
    for item in proteins:
        if item not in proteins_set:
            proteins_set.add(item) 
    for item in proteins_set:
        print(item)

   

