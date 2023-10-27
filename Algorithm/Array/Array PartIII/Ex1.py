# Ex1 - Array string
arr = ['banana','coconut','mango','jackfruit']

#1 - Count letter each item (function)
[6,7,5,9]
def Sumitems(arr):
    sum=0
    for i in range(len(arr)):
        word=arr[i]
        sum=0
        for j in range(len(word)):
            sum+=1
        arr[i]=sum
    return arr
arr = ['banana','coconut','mango','jackfruit']
print(Sumitems(arr))
#2 - Reverse string in list (function)
# def ReverseLetter(arr):
#     result=""
#     for i in range(len(arr)):
#         word=arr[i]
#         for j in range(len(word)):
#             result+=word[-1-j]
#         arr[i]=result
#         result=""
#     return arr
# arr = ['banana','coconut','mango','jackfruit']
# print(ReverseLetter(arr))
# ['ananab', 'tunococ', ...]

#3 - Count letter "n" in list (function)
# [2, 1, 1, 0]
# def FindLetterN(arr):
    
#     for i in range(len(arr)):
#         word=arr[i]
#         count=0
#         for j in range(len(word)):
#             if word[j]=="n":
#                 count+=1
#         arr[i]=count
#     return arr
# arr = ['banana','coconut','mango','jackfruit']
# print(FindLetterN(arr))
#4 - Get last letter in each item (function)
['a', 't', 'o', 't']
arr = ['banana','coconut','mango','jackfruit']
result=[]
for i in range(len(arr)):
    result+=(arr[i][-1])
print(result)
# 5 - Add new fruit to list (function)
# function name: addNewFruit(arr, newFruit)
# def addNewFruit(arr,NewFruit):
#     arr.append(NewFruit)
#     return arr
# NewFruit='Strawberry'
# print(addNewFruit(arr,NewFruit))
# ['banana','coconut','mango','jackfruit', 'orange']

#6 - Concate first text together
# bcmj
# arr = ['banana','coconut','mango','jackfruit']
arr="bcmj"
print(arr)