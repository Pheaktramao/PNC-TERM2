text=input()
result=""
for i in range (len(text)):
    if text[0]<text[i]:
        result="STORED"
    elif text[0]>text[i]:
        result="NOT STORED"
print(result)