text=input()
sum=0
result=""
isSeven=False
for i in range(len(text)):
    if text[i]=="7" and not isSeven:
        result=""
        isSeven=True
    else:
        if isSeven and text[i]!="7":
            sum+=int(text[i])
print(sum)