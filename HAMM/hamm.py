with open("rosalind_hamm.txt") as f:
    s,t = [x.strip() for x in f.readlines()]
diffs=0
for i in range(len(s)):
    if s[i]!=t[i]:
        diffs+=1
print(diffs)
