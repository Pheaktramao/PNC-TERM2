# Ex1 - Array string
#1 - Remove duplicate name from list
# def CheckValue(Value,list):
#     isUnique=False
#     for i in range(len(list)):
#         if Value .lower()==list[i].lower():
#             isUnique=True
#     return isUnique
# arr=["Rady","yon","mengheang", "rady", "Yon"]
# list=[]
# for i in range(len(arr)):
#     if  not CheckValue(arr[i],list):
#         list.append(arr[i])
# print(list)
#2 - Reverse only "mengheang" name in list
# arr=["Rady","yon","mengheang", "rady", "Yon"]
# for i in range(len(arr)):
#     if arr[i]=="mengheang":
#         word=arr[i]
#         result=""
#         for j in range(len(word)):
#             result+=word[-1-j]
#         arr[i]=result
# print(arr)
#3 - Add "Ronan" to first index
# arr=["Rady","yon","mengheang", "rady", "Yon"]
# arr.insert(0,"Ronan")
# print(arr)
#4 - Create new list with number of character in list
# arr=["Rady","yon","mengheang", "rady", "Yon"]
# for i in range(len(arr)):
#     word=arr[i]
#     count=0
#     for j in range(len(word)):
#         count+=1
#     arr[i]=count
# print(arr)
[4, 3, 9, 4, 3]

#5 - Create new list with letter "a", "e", "i", "o", "u"
['a','o', 'e', 'e', 'a', 'a', 'o']

#6 - Count number of 'A' in list
arr=["Rady","yon","mengheang", "rady", "Yon"]
# for i in range(len(arr)):
#     word=arr[i]
#     countA=0
#     for j in range(len(word)):
#         if word[j]=="A" or word[j]=="a":
#             countA+=1
#     arr[i]=countA
# print(arr)
[1, 0, 1, 1, 0]

#7 - Keep name who start from letter "R" only
arr=["Rady","yon","mengheang", "rady", "Yon"]
# array=[]
# for i in range(len(arr)):
#     word=arr[i]
#     if word[0].upper()=='R':
#         array.append(arr[i])
# print(array)
#8 - Remove "Mengheag" from list
arr=["Rady","yon","mengheang", "rady", "Yon"]

# arr=["Rady","yon","mengheang", "rady", "Yon"]
#9 - Create nested array (Array 2D) from list
# def creatNewArray(word):
#     newArray=[]
#     for i in range(len(word)):
#         newArray.append(word[i])
#     return newArray

# arr=["Rady","yon","mengheang", "rady", "Yon"]
# newaray2D=[]
# for i in range(len(arr)):
#     newaray2D.append(creatNewArray(arr[i]))
# print(newaray2D)
[ ['R','a','d','y'], ['y','o','n'], ...]