text=input()
result=""
for i in range(len(text)):
    if text[0]<text[i] :
        result="SORTED"
    elif text[0]==text[i]:
        result="SORTED"
    else:
        result="NOT SORTED"
print(result)