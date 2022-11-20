import networkx as nx

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


with open('rosalind_dbru.txt','r') as f:
    dnas=f.readlines()
S=set([item.strip() for item in dnas])
k=len(list(S)[0])


S_rc=[]
for item in S:
    item_revc=funcREVC(item)
    S_rc.append(item_revc)

S_U_Src=S.union(set(S_rc))

node_list=[]
for item in S_U_Src:
    first_k=item[:k-1]
    second_k=item[1:]
    node_list.append(first_k)
    node_list.append(second_k)
    
G=nx.DiGraph()
for node in set(node_list): 
    G.add_node(node)

for item in S_U_Src:
    G.add_edge(item[:k-1],item[1:])

f = open("dbru_out.txt", "w")
for item in list(G.edges):
    f.write('('+item[0]+', '+item[1]+')'+'\n')  
f.close


