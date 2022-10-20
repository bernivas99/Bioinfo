
def func5(s):
    word_dict ={}
    stringlist = s.strip().split(' ')
    for item in stringlist:
        if item not in word_dict.keys():
            word_dict[item]=1
        else:
            word_dict[item]+=1
    for key, value in word_dict.items():
        print(key,value)
        

with open('rosalind_ini6.txt') as f:
    t= f.readlines()[0]
func5(t)
