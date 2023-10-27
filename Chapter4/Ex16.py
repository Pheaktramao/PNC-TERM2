# Ex6 - Array
arr = ['banana','coconut','mango','Jackfruit','orange','apple']
# def reverString(word):
#     lastIndex = len(word) - 1
#     result = ""
#     for i in range(len(word)):
#         result += word[lastIndex - i]
#     return result
# def oneLetterA(word):
#     counter = 0
#     isOne = False
#     for i in range(len(word)):
#         if word[i].lower() == 'a':
#             counter += 1
#     if counter == 1:
#         isOne = True
#     return isOne
# newArr = []
# for i in range(len(arr)):
#     if oneLetterA(arr[i]):
#         newArr.append(reverString(arr[i]))
#     else:
#         newArr.append(arr[i])
# print(newArr)
#1 - Reverse only text contain 1 letter A

#2 - Count letter A in text
# newArr=[]
# word=""
# for i in range(len(arr)):
#     word=arr[i]
#     count=0
#     for j in range(len(word)):
#         if word[j].lower()=='a':
#             count+=1
#     newArr.append(count)
# print(newArr)
# [3, 0, 1, 1, 1, 1]
#3 - Replace letter A with * in text
def replace_letter(word):
    result=""
    for i in range(len(word)):
        if word[i].lower()=='a':
            result+='*'
        else:
            result+=word[i]
    return result
arr = ['banana','coconut','mango','Jackfruit','orange','apple']
newArr=[]
for i in range(len(arr)):
    newArr.append(replace_letter(arr[i]))
print(newArr)
# text='Pheaktra'
# res=""
# for i in range(len(text)):
#     if text[i]=='a':
#         res+='*'
#     elif text[i]!='a':
#         res+=text[i]
# print(res)