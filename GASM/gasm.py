import networkx as nx
from itertools import combinations_with_replacement, permutations

def funcREVC(t):
    new_t=t[::-1]
    newstr=''
    for letter in new_t:
        if letter=='A':
            newstr=newstr+'T'
        elif letter=='T':
            newstr=newstr+'A'
        elif letter=='C':
            newstr=newstr+'G'
        elif letter=='G':
            newstr=newstr+'C'
    return newstr

def generate_all_combos(alphabet,n):
    all_combos=[]
    combi_list=list(combinations_with_replacement(alphabet,n))
    for item in combi_list:
        perm=permutations(item)
        all_combos=all_combos+list(perm)
    combi=set(all_combos)
    return combi


with open('rosalind_gasm.txt','r') as f:
    lines=f.readlines()
lines=[item.strip() for item in lines]
k=len(lines[0])


for l in range(k-1,1,-1): 
    G=nx.DiGraph()
    
    reads=[]
    for item in lines:
        for i in range(k-l+1):
            reads.append(item[i:i+l])
            reads.append(funcREVC(item[i:i+l]))
    reads=set(reads)
    

    for node in reads: 
        G.add_node(node)
    for item1 in reads:
        for item2 in reads:
            if item2[:l-1]==item1[1:]:
                G.add_edge(item1,item2)
    cycles=sorted(nx.simple_cycles(G))
    if len(cycles)==2:
        break

results=[]
for cycle in cycles:
    shortest=cycle[0]
    for i in range(1,len(cycle)):
        shortest=shortest+cycle[i][len(cycle[i])-1]
    shortest_circular=shortest[:len(shortest)-l+1]
    results.append(shortest_circular)

print(results[0])
