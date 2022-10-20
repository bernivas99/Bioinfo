def func4(filename):
    even_lines = []
    with open(filename) as f:
        lines = f.readlines()
        for i in range(len(lines)):
            if i%2==0:
                print(lines[i+1].rstrip()) 

func4("rosalind_ini5.txt")