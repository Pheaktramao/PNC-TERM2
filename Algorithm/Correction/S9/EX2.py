text=input()
result=""
for i in range(len(text)-2):
    if text[i]=="a" and text[i+1]=="b" and text[i+2]=="c":
        result="Ok"
    else:
        result="WRONG"
print(result)