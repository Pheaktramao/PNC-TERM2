text=input()
indexofK=0
isTrue=False
i=0
for i in range(len(text)):
    if text[i]=='K' or text[i]=='k':
        indexofK=i
        isTrue=True
if isTrue:
    print(indexofK)
else:
    print(-1)

text=input()
indexofK=0
isTrue=False
i=0
while i<len(text) and not isTrue:
    if text[i]=="k":
        indexofK=i
        isTrue=True
    i+=1
if isTrue:
    print(indexofK)
else:
    print(-1)

# text = input()
# result = -1
# is_finished = False
# for index in range(len(text)) :
#     letter = text[index]
#     if letter == "K" and is_finished:
#         result = index
#         is_finished = True
# print(result)