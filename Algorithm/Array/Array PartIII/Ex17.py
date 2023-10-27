# Ex1 - String
text = "aba is the bank in cambodia"
#1 - add text to array
word=""
array=[]
for i in range(len(text)):
    if text[i]==" " or i==len(text)-1:
        word+=text[i]
        array.append(word)
        word=""
    else:
        word+=text[i]
print(array)
# ['aba', 'is', 'the', 'bank', 'in', 'cambodia']
# 2 - Find first index of "B"
index=None
i=0
isFound=False
while i<len(text) and not isFound:
    if text[i]=='b':
        index=i
        isFound=True
    i+=1
print(index)
# #3 - Convert text to capitalize
# "Aba Is The Bank In Cambodia"
isuppercase=False
result=""
for i in range(len(text)):
    if i==0:
        result+=text[i].upper()
    elif isuppercase:
        result+=text[i].upper()
        isuppercase=False
    elif text[i]==" ":
        result+=text[i]
        isuppercase=True
    else:
        result+=text[i]
print(result)
#4 - Reverse word by word
# "aba si eht knab ni aidobmac"
 