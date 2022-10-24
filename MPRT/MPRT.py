#orai: MPRT,FIB,IPRB
#házi: ORF, PRTM

import requests
from io import StringIO
from Bio import SeqIO


try:
    with open("rosalind_mprt.txt") as f:
        for line in f:
            id_line = line[:6]
            resp=requests.get("https://rest.uniprot.org/uniprotkb/{}.fasta".format(id_line))
            indexes=[]
            exists=False
            fasta_io = StringIO(resp.text) 
            record_dict = SeqIO.parse(fasta_io, "fasta") 
            for rec in record_dict:
                protein = rec.seq

            for i in range(len(protein)-4):
                if protein[i]=='N' and protein[i+1]!='P' and (protein[i+2]=='S' or protein[i+2]=='T' ) and protein[i+3]!='P':
                    exists=True
                    indexes.append(i+1)

            if exists:
                print(line.strip())
                for item in indexes:
                    print(item,sep=' ', end=' ', flush=True)
                print("\r")
except FileNotFoundError:
    print('There is no such file')
    