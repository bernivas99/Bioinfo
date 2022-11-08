from itertools import combinations_with_replacement,permutations

def generate_all_combos(alphabet,n):
    all_combos=[]
    combi_list=list(combinations_with_replacement(alphabet,n))
    for item in combi_list:
        perm=permutations(item)
        all_combos=all_combos+list(perm)
    combi=set(all_combos)
    return combi


with open("rosalind_lexf.txt","r") as f:
    alphabet=f.readline().strip().split(' ')
    n=int(f.readline().strip())
str_from_alphabet="".join(alphabet) 
combi_list=generate_all_combos(str_from_alphabet,n)

words=[]
for word in combi_list:
    words.append("".join(word))
words.sort()
for word in words:
    print(word)