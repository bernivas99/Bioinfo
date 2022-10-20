def funcREVC(filename):
    with open(filename) as f:
        t = f.readlines()[0]
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
    print(newstr)

funcREVC('rosalind_revc.txt')