def funcDNA(filename):
    with open(filename) as f:
        s = f.readlines()[0]

    letter_dict={}
    for letter in s:
        if letter not in letter_dict:
            letter_dict[letter]=1
        else:
            letter_dict[letter]+=1
    print(letter_dict['A'],letter_dict['C'],letter_dict['G'],letter_dict['T'])


funcDNA("rosalind_dna.txt")