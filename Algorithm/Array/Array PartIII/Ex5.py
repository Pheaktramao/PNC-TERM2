# Ex3 - Array
# arr = [6, 4, 3, 4]
#1 - Sum first index with last  index
# sum=0
# sum=arr[0]+arr[len(arr)-1]
# print(sum)
# result = 10
#2 - Square all number (function)

# def SquareItems(arr):
#     Square=1
#     NewArray=[]
#     for i in range(len(arr)):
#         number=int(arr[i])
#         Square=number*number
#         NewArray.append(Square)
#     Square=1
#     return NewArray
# arr = [6, 4, 3, 4]
# print(SquareItems(arr))
# [36, 16, 9, 16]
# #3 - Remove duplicate from list (function)
def chekValue(Value,list):
    isFound=True
    for i in range(len(list)):
        if Value==list[i]:
            isFound=False
    return isFound
arr = [6, 4, 3, 4]
list=[]
for i in range(len(arr)):
    if not chekValue(arr[i],list):
        list.append(arr[i])
print(list)
# [6, 3, 4]
# #4 - create 2D array follow number in list
# [
#   [1, 2, 3, 4, 5, 6],
#   [1, 2, 3, 4]
#   [1, 2, 3],
#   [1, 2, 3, 4]
# ]