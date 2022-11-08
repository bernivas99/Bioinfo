import networkx as nx

edges=[]
with open("rosalind_tree.txt","r") as f:
    n=int(f.readline())
    for line in f.readlines():
        edge=line.strip().split(' ')
        edge=[int(x) for x in edge]
        edges.append(edge)

G=nx.Graph()
G.add_nodes_from(range(1,n+1))
G.add_edges_from(edges)

no_comps=nx.number_connected_components(G)

print(no_comps-1)
