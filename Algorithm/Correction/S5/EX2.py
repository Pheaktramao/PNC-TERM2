# text=input()
# result=""
# for i in range(len(text)):
#     if text[0]<text[i]:
#         result=True
#     elif text[i]<text[0]:
#         result=False
#     else:
#         result=False
# print(result)

# text=input()
# result=""
# for i in range(len(text)):
#     if text[i]>"6":
#         result=True
#     elif text[i]<"6":
#         result=False
# print(result)

text=input()
result=""
for i in range(len(text)):
    for j in range(len(text)):
        if j>=i and j<(len(text)-i):
            result+=text[j]
    result+="\n"
print(result)