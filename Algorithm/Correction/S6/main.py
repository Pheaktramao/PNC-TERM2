# text1="I AM RONAN AND I WORK WITH RADY"
# text2=""
# for i in range(len(text1)):
#     char=text1
#     if char !="A":
#         text2+=char
# print(text1)
# print(text2)

text=input()
word=" "
isfound=False
for i in range(len(text)):
    if text[i]==" " or i==len(text)-1:
        if i ==len(text)-1:
            word+=text[i]
        if word.upper()=="RADY":
            isfound=True
        word=""
    else:
        word+=text[i]
if isfound:
    print("Yes")
else:
    print("No")