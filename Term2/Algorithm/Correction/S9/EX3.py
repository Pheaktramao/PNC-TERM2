# text=input()
# result=""
# isSign=False
# iscorrect=False
# for i in range(len(text)):
#     if text[i]=="[":
#         isSign=True
#     else:
#         if isSign and text[i]!="[":
#             result+=text[i]
#     if text[i]=="]":
#         isSign=False
#         iscorrect=True
# if iscorrect:
#     print("OK")
# else:
#     print("WRONG")


text=input()
word=""
reault=""
isSign=False
isY=False
for i in range(len(text)):
        if text[i]=="[" and not isSign:
                isSign=True
        else:
                if isSign and text[i]!="]":
                        if text[i]=="Y" or text[i]=="y":
                                word+=text[i]
                                isY=True
                elif text[i]!="]":
                        isSign=False
                else:
                        if text[i]=="]":
                                isSign=False
if isY:
        result="OK"
else:
        result="WRONG"
print(result)