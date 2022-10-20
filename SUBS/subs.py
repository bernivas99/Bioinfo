with open('rosalind_subs.txt') as f:
    s, t = f.readlines()
    s=s.strip('\n')
    t=t.strip('\n')
l=len(t)
for i in range(len(s)):
    substring=s[i:i+l]
    if substring==t:
        print(i+1)