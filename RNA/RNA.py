def funcRNA(filename):
    with open(filename) as f:
        t = f.readlines()[0]
    new_t=t.replace('T', "U")
    print(new_t)

funcRNA('rosalind_rna.txt')