import networkx as nx
from Bio import SeqIO

record_dict = SeqIO.to_dict(SeqIO.parse("rosalind_grph.txt", "fasta"))

def with_nx(record_dict):
    G=nx.DiGraph()
    for key, value in record_dict.items():
        G.add_node(key)
    for key1, value1 in record_dict.items():
        for key2, value2 in record_dict.items():
            if str(value1.seq[len(value1.seq)-3:len(value1.seq)])==str(value2.seq[0:3]) and key1!=key2:
                G.add_edge(key1,key2) 
    #G.remove_edges_from(nx.selfloop_edges(G))
    return list(G.edges)



def without_nx(record_dict):
    pairs= []
    for key1, value1 in record_dict.items():
        for key2, value2 in record_dict.items():
            if str(value1.seq[len(value1.seq)-3:len(value1.seq)])==str(value2.seq[0:3]) and key1!=key2:
                a_pair=(key1,key2) 
                pairs.append(a_pair)
    return pairs

basic_list=without_nx(record_dict)
nx_list=with_nx(record_dict)
for item in nx_list:
    print(item[0],item[1])


