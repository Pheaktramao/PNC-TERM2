text=input()
sum=0
i=0
isSeven=False
while i<len(text) and not isSeven:
    if text[i]!="7":
        sum+=int(text[i])
    i+=1
else:
    isSeven=True
print(sum)