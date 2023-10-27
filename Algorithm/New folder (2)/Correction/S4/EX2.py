text=input()
isFound=False
result=0
i=0
while i<len(text) and not isFound:
    if text[i]=='o' or text[i]=='O':
        result=i
        isFound=True
    i+=1
if isFound:
    print(result)
else:
    print(-1)

text=input()
isFound=True
result=-1
for i in range(len(text)):
    if text[i]=='o' and isFound:
        result=i
        isFound=False
print(result)