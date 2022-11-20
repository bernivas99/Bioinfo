import networkx as nx


with open('rosalind_pcov.txt','r') as f:
    lines=f.readlines()
lines=[item.strip() for item in lines]

k=len(lines[0])

node_list=[]
for item in lines:
    first_k=item[:k-1]
    second_k=item[1:]
    node_list.append(first_k)
    node_list.append(second_k)
    
G=nx.DiGraph()
for node in set(node_list): 
    G.add_node(node)

for item in lines:
    G.add_edge(item[:k-1],item[1:])

cycle=sorted(nx.simple_cycles(G))[0]

shortest=cycle[0]
for i in range(1,len(cycle)):
    shortest=shortest+cycle[i][len(cycle[i])-1]

shortest_circular=shortest[:len(shortest)-k+2]
print(shortest_circular)