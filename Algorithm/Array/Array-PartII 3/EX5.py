# Ex5 - Array (While loop only)
# arr = ['A','A','B','B','C','A','C']
#1 - Create to new list to remove duplicate value
# def checkValue(value,list):
#     isUnique=False
#     i=0
#     while i<len(list) and not isUnique:
#         if value==list[i]:
#             isUnique=True
#         i+=1
#     return isUnique
# arr = ['A','A','B','B','C','A','C']
# list=[]
# i=0
# while i<len(arr): 
#     if not checkValue(arr[i],list):
#         list.append(arr[i])
#     i+=1
# print(list)
#2 - If A = 10, B = 20, C = 30 how many value in list in total
# i=0
# total=0
# while i<len(arr):
#     if arr[i]=="a" or arr[i]=="A":
#         total+=10
#     elif arr[i]=="b" or arr[i]=="B":
#         total+=20
#     elif arr[i]=="c" or arr[i]=="C":
#         total+=30
#     i+=1
# print(total)
#3 - Filter new list and keep letter "A" only
# i=0
# NewArray=[]
# while i<len(arr):
#     if arr[i]=="A":
#         NewArray.append(arr[i])
#     i+=1
# print(NewArray)
# Ex6 - Array (While loop only)
arr = [1, 10, 168, 190, 2024, 120393]
#1 - Remove 2024 from list
# i=0
# index=0
# while i<len(arr):
#     if arr[i]==2024:
#         index=i
#     i+=1
# arr.pop(index)
# print(arr)
#2 - How many degit from each item
# i=0
# NewArray=[]
# while i<len(arr):
#     number=str(arr[i])
#     n=len(number)
#     NewArray.append(n)
#     i+=1
# print(NewArray)
# [1, 2, 3, 3, 4, 6]
#3 - replace all item that have degit greater than 3 by 100
i=0
while i<len(arr):
    if arr[i]>3:
        arr[i]=100
    i+=1
print(arr)
# [1, 10, 100, 100, 100, 100]