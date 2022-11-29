with open('rosalind_asmq.txt','r') as f:
    dnas=f.readlines()
dna_strings=[item.strip() for item in dnas]


total_sum=0
for item in dna_strings:
    total_sum+=len(item)

max_length=max([len(item) for item in dna_strings])

L50,L75=0,0
got_L50,got_L75= False,False
for i in range(max_length,1,-1):
    sums_of_nucl=0
    for item in dna_strings:
        if len(item)>=i:
            sums_of_nucl+=len(item)
    if sums_of_nucl>=0.5*total_sum and got_L50==False:
        L50=i
        got_L50=True
    if sums_of_nucl>=0.75*total_sum and got_L75==False:
        L75=i
        got_L75=True

print(L50,L75)
