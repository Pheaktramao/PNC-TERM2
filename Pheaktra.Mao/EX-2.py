Array=eval(input())
isFound=False
newArr=[]
for i in range (len(Array)):
    word=str(Array[i])
    j=0
    count=0
    while j<len(word) and not isFound:
        if word[j]=='e' or word[j]=='E':
            isFound=True
        elif isFound:
            if word[j]=='e' or word[j]=='E' and isFound:
                isFound=False
        else:
            isFound=False
print(newArr)