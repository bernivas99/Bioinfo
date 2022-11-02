import math

with open("rosalind_prob.txt") as f:
    s,x_str = [x.strip() for x in f.readlines()]
x_array=[float(x) for x in x_str.split(' ')]

b_array=[]
for x in x_array:
    logsum=0
    for char in s:
        if char=='C' or char=='G':
            logsum+=math.log10(x/2)
        elif char=='A' or char=='T':
            logsum+=math.log10((1-x)/2)
    b_array.append(logsum)
for item in b_array:
    print(item, end=' ')