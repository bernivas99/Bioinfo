monois = {}
with open("monoisotopic-mass-table.txt") as f:
    for line in f:
        key, value = line.split()
        monois[key] = float(value)

with open("rosalind_prtm.txt") as f:
    line = f.readlines()[0].strip()
    
szumma=0
for char in line:
    szumma+=monois[char]
print(szumma)