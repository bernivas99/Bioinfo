def func1(a,b):
    return a**2+b**2

def func2(s,a,b,c,d):
    return s[a:b+1]+" "+s[c:d+1]

def func3(a,b):
    szumma=0
    for i in range(a,b+1):
        if i%2==1:
            szumma+=i
    return szumma

def func4(filename):
    even_lines = []
    f = open(filename, "r")
    lines = f.readlines()
    for i in range(len(lines)):
        if i%2==0:
            print(lines[i+1].rstrip()) #0-tól indexelődnek, de mi 1-től tekintjűk

def func5(s):
    word_dict ={}
    stringlist = s.split(' ')
    for item in stringlist:
        if item not in word_dict.keys():
            word_dict[item]=1
        else:
            word_dict[item]+=1
    for key, value in word_dict.items():
        print(key)
        print(value)

            
    
print(func1(3,5))
print(func2("HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.",22,27,97,102))
print(func3(100,200))
func4("rosalind_ini5.txt")
func5("When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be")
