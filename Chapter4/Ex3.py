# Ex1 - String
numberInString = "10 30 4 12"
#1 - How many number in string
# sum=0
# for i in range(len(numberInString)):
#     if numberInString[i].isnumeric():
#         sum+=1
# print(sum)
#2 - Sum all value seperated by space 
# result=""
# sum=0
# for i in range(len(numberInString)):
#     if numberInString[i]!=" " :
#         result+=numberInString[i]
#     elif result.isnumeric():
#         sum+=int(result)
#         result=''
# sum+=int(result)
# print(sum) 
#3 - Find average of number
# result=""
# sum=0
# average=0
# for i in range(len(numberInString)):
#     if numberInString[i]!=" " :
#         result+=numberInString[i]
#     elif result.isnumeric():
#         sum+=int(result)
#         result=''
# sum+=int(result)
# average=sum/len(numberInString)
# print(average) 
# ------------
# Ex2 - String
text = "Welcome to Phnom Penh"
#1 - how amny letter in string
counLetter=0
for i in range(len(text)):
    if text[i]!=" ":
        counLetter+=1
print(counLetter)
#2 - Reverse string
result=""
for i in range(len(text)):
    result+=text[-1-i]
print(result)
#3 - add string to arr : ['welcome', 'to', 'phnom', 'penh']
Arr=[]
word=""
for i in range(len(text)):
    if text[i]!=" ":
            word+=text[i]
    else:
        Arr.append(word)
        word=""
Arr.append(word)
print(Arr)
# ----------