# # Ex1 - Array
# # String to array
# # Input: Hello
# Output: ['H','e','l','l','o']
# text=input("Enter word:")
# Array=[]
# for i in range(len(text)):
#     Array.append(text[i])
# print(Array)
# # ------------------
# # Ex2 - Array
# # String to array seperate by space
# Input: aba bank in Cambodia
# output: ['aba', 'bank','in','Cambodia']
# text=input("Enter text:")
# newArr=[]
# word=""
# for i in range(len(text)):
#     if text[i]==" " or i==len(text)-1:
#         word+=text[i]
#         newArr.append(word)
#         word=""
#     else:
#         word+=text[i]
# print(newArr)
# ------------------
# Ex3 - Array
# # Get only text contains letter A
# Input: ['banana','coconut','mango']
# output: ['banana','mango']
# Array=eval(input())
# for i in range(len(Array)):
#     word=Array[i]
#     bool=False
#     for j in range(len(word)):
#         if word[j]=='a' and not bool:
#             Array.append(word[j])
#         bool=True
# print(Array)
# ------------------
# Ex4 - Array
# # Reverse array and reverse text in array
# Input: ['banana','coconut']
# output: 
# ['coconut','banana']
# ['ananab','tunococ']
# Array=eval(input())
# newArr=[]
# for i in range(len(Array)):
#     word=Array[i]
#     result=""
#     for j in range(len(word)):
#         result+=word[-1-j]
#     newArr.append(result)
#     result=""
# print(newArr)
# ------------------
# Ex5 - Array
# #Count number
# Input1: [2, 2, 3, 5, 2, 3, 2, 5, 8]
# Input2: [2, 3]
# Output: [ { 2: 4} , {3: 2} ]
# def count_number(list,Value):
#     count=0
#     for i in range(len(list)):
#         if list[i]==Value:
#             count+=1
#     number={}
#     number[Value]=count
#     return number
# Narr=eval(input("Enter array:"))
# Nfind=eval(input("Enter array:"))
# newArr=[]
# for i in range(len(Nfind)):
#     newArr.append(count_number(Narr,Nfind[i]))
# print(newArr)
# ------------------
# Ex6 - Array
# # Array to object
# input: ['banana','coconut', 'mango', 'orange']
# output: 
# [
#   {0: 'banana',1: 'coconut',2: 'mango',3: 'orange'}
# ]

# --------------
# Ex7 - Array
# # Array to object - counting character
# input: ['banana','coconut', 'mango', 'orange']
# output: 
# [
#   {'banana':6,'coconut':7,'mango': 5,'orange': 6}
# ]
def count_character(word):
    count=0
    for i in range(len(word)):
        count+=1
    CountCha={}
    CountCha[word]=count
    return CountCha
arr=eval(input())
newArr=[]
for i in range(len(arr)):
    newArr.append(count_character(arr[i]))
print(newArr)
# --------------