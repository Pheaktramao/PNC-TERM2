text=input()
word=""
isFound=False
for i in range(len(text)):
    if text[i]==" " or i==len(text)-1:
        if i==len(text)-1 and text[i]!="." and text[i]!="!" and text[i]!="?":
            word+=text[i]
        if word.upper()=="rady":
            isFound=True
        word=""
    else:
        if text[i]!="." and text[i]!="!" and text[i]!="?":
            word+=text[i]
print(word)