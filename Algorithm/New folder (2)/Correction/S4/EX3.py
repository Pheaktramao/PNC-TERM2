word1=input()
word2=input()
result1=0
result2=0
result=0
for i in range(len(word1)):
    if word1[i].isupper():
        result1+=1
for i in range(len(word2)):
    if word2[i].isupper():
        result2+=1
result=result1+result2
print(result)