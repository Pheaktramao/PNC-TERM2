text=input()
result=""
isfound=False
for i in range(len(text)):
    if text[i]==" " and i==len(text)-1:
        if text[i].isupper()=="RADY":
            result="Yes"
            isfound=True
        else:
            result="No"
print(result)