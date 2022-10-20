from Bio import SeqIO

def overlap( str1, str2 ):
    concatenated=''
    length=-1
    for i in range( 1, min( len(str1), len(str2) ) ):
            if str1[-i:] == str2[:i]:
                concatenated= str1 + str2[i:]
                length=i
    return length, concatenated


record_dict = SeqIO.to_dict(SeqIO.parse("rosalind_long.txt", "fasta"))
for key, value in record_dict.items():
    record_dict[key]=str(value.seq)


while len(record_dict)>1:
    max_length_of_overlap=0
    max_concatenated=''
    for key1, value1 in record_dict.items():
        for key2, value2 in record_dict.items():
            #print('strings',value1.seq,value2.seq)
            length, concatenated =overlap(value1,value2)
            if length>max_length_of_overlap:
                max_length_of_overlap=length
                max_str1= key1
                max_str2=key2
                max_concatenated=concatenated
    del record_dict[max_str1]
    del record_dict[max_str2]
    record_dict[max_str1]=max_concatenated
print(record_dict[max_str1])
