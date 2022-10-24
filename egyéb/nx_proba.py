import networkx as nx
import sys, os

dn=os.path.dirname(__file__)
pdn= os.path.join(dn,"")
sys.path.append(pdn)

import requests
resp=requests.get("https://rest.uniprot.org/uniprotkb/A0PK11.fasta")
print(resp.text)