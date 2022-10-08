from Bio import SeqIO

#for seq_record in SeqIO.parse("rosalind_gc.txt", "fasta"):
    #print(seq_record.id)
    #print(repr(seq_record.seq))
    #print(len(seq_record))

    
record_dict = SeqIO.to_dict(SeqIO.parse("rosalind_gc.txt", "fasta"))

max_percentage=0
max_id=''
for key, value in record_dict.items():
    content=0
    for letter in value:
        if letter=='C' or letter=='G':
            content+=1
    if (content/len(value))>=max_percentage:
        max_percentage=(content/len(value))
        max_id=key
print(max_id, max_percentage*100)