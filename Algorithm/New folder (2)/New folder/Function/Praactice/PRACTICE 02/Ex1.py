# text=input()
# sum=0
# for i in range(len(text)):
#     if text[i]!=" " :
#         if text[i].isupper():
#             sum+=1
# print(sum)

def NumberofUppercase(string):
    sum=0
    for i in range(len(string)):
        if string[i]!=" ":
            if string[i].isupper():
                sum+=1
    return sum
text=input()
print(NumberofUppercase(text))