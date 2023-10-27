def reverseText(text):
    result=""
    lastIndex=len(text)-1
    for i in range(len(text)):
        result+=text[lastIndex-i]
    return result
Array=eval(input())
newArr=[]
lastIndex=len(Array)-1
for i in range(len(Array)):
    newArr.append(reverseText(Array[lastIndex-i]))
print(newArr)