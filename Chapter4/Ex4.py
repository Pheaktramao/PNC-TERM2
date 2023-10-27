# Ex3 - Array number
arr = [10, 3, 4, 8, 9, 4, 5, 3, 5]
#1 - Reverse array
# NewArr=[]
# for i in range(len(arr)):
#     NewArr.append(arr[-1-i])
# print(NewArr)
#2 - Remove duplicate value
# def removeValue(Value,list):
#     isFound=False
#     for i in range(len(list)):
#         if list[i]==Value:
#             isFound=True
#     return isFound
# arr = [10, 3, 4, 8, 9, 4, 5, 3, 5]
# list=[]
# for i in range(len(arr)):
#     if not removeValue (arr[i],list):
#         list.append(arr[i])
# print(list)
#3 - replace numebr > 3 with 0
# for i in range(len(arr)):
#     if arr[i]>3:
#         arr[i]=0
# print(arr)
#4 - Find average of odd number
# def find_average(arr):
#     sum=0
#     average=0
#     for i in range(len(arr)):
#         if arr[i]%2!=0:
#             sum+=arr[i]
#     average=sum/len(arr)
#     return average
# arr = [10, 3, 4, 8, 9, 4, 5, 3, 5]
# print(find_average(arr))
#6 - remove number 8, 9, 10
def removeNumber(value,arr):
    index=None
    for i in range(len(arr)):
        if arr[i]==value:
            index=i
        arr.pop(index)
    return arr
arr = [10, 3, 4, 8, 9, 4, 5, 3, 5]
value=int(input())
print(removeNumber(8,arr))
# ----------