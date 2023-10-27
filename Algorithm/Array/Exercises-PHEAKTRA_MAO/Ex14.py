# Ex1 - String
# text = "38347"
#1 - Sum all number in string (function)
# def sumNumber(text):
#     sum=0
#     for i in range(len(text)):
#         sum+=int(text[i])
#     return sum
# text = "38347"
# print(sumNumber(text))
# #2 - Find average of number in string (function)
# def averageNumber(text):
#     sum=0
#     aver=0
#     for i in range(len(text)):
#         sum+=int(text[i])
#     aver=sum/len(text)
#     return aver
# text = "38347"
# print(averageNumber(text))
# #3 - Reverse the string (function)
# # def reversestring(text):
# #     result=""
# #     for i in range(len(text)):
# #         result+=text[-1-i]
# #     return result
# # text = "38347"
# # print(reversestring(text))
# # ------------------------------
# # Ex2 - Array
# # arr = [10, 12, 3, 8, 9, 12, 12, 10, 10]

# #1 - Sum all number (function)
# # def sumNumber(array):
# #     sum=0
# #     for i in range(len(array)):
# #         sum+=array[i]
# #     return sum
# # arr = [10, 12, 3, 8, 9, 12, 12, 10, 10]
# # print(sumNumber(arr))
# # #2 - Reverse array (function)
# # def ReverseArray(array):
# #     Newarray=[]
# #     for i in range(len(array)):
# #         Newarray.append(array[-1-i])
# #     return Newarray
# # arr = [10, 12, 3, 8, 9, 12, 12, 10, 10]
# # print(ReverseArray(arr))
# # #3 - Find index of 3 (function)
# # def findIndex(array):
# #     index=0
# #     for i in range(len(array)):
# #         if array[i]==3:
# #             index=i
# #     return index
# # arr = [10, 12, 3, 8, 9, 12, 12, 10, 10]
# # print(findIndex(arr))
# # #4 - Romove 8 number from list (function)
# # def RemoveNumber(array):
# #     index=0
# #     for i in range(len(array)):
# #         if array[i]==8:
# #             index=i
# #     array.pop(index)
# #     return array
# # arr = [10, 12, 3, 8, 9, 12, 12, 10, 10]
# # print(RemoveNumber(arr))
# # #5 - Remove duplicate value (function)
# # def FindValue(Value,list):
# #     isTrue=True
# #     for i in range(len(list)):
# #         if Value==list[i]:
# #             isTrue=False
# #     return isTrue
# # arr = [10, 12, 3, 8, 9, 12, 12, 10, 10]
# # list=[]
# # for i in range(len(arr)):
# #     if  FindValue(arr[i],list):
# #         list.append(arr[i])
# # print(list)
# # #6 - Replace 10 by 99
# # arr = [10, 12, 3, 8, 9, 12, 12, 10, 10]
# # for i in range(len(arr)):
# #     if arr[i]==10:
# #         arr[i]=99
# # print(arr)
# # -------------------------------
# # Ex3 - Array 2D
# arr = [
#   [1, 2, 3],
#   [2, 3, 4],
#   [5, 6, 8],
#   [10, 3, 8]
# ]
# #1 - How many number 2 in list
# count=0
# for i in range(len(arr)):
#     array=arr[i]
    
#     for j in range(len(array)):
#         if array[j]==2:
#             count+=1
# print(count)
# #2 - Sum only number > 5
# sum=0
# for i in range(len(arr)):
#     array=arr[i]
#     for j in range(len(array)):
#         if array[j]>5:
#             sum+=array[j]
# print("Number greater than 5: "+str(sum))
# #3 - How many number < 5
# def sumNumber(Array):
#     sum=0
#     for i in range(len(Array)):
#         array=Array[i]
#         for j in range(len(array)):
#             if array[j]<5:
# #                 sum+=array[j]
# #     return sum
# # arr = [
# #   [1, 2, 3],
# #   [2, 3, 4],
# #   [5, 6, 8],
# #   [10, 3, 8]
# # ]
# # print(sumNumber(arr))
# #4 - Sum number in row
# def sum_number(array):
#     sum=0
#     for i in range(len(array)):
#         sum+=array[i]
#     return sum
# arr = [
#   [1, 2, 3],
#   [2, 3, 4],
#   [5, 6, 8],
#   [10, 3, 8]
# ]
# Newarray=[]
# for i in range(len(arr)):
#     Newarray.append(sum_number(arr[i]))
# print(Newarray)
# #5 - Sum number in column
# def sum_column(array):
    
#     Newarray=[]
#     for i in range(len(array[0])):
#         sum=0
#         for j in range(len(array)):
#             sum+=array[j][i]
#         Newarray.append(sum)
#         sum=0
#     return Newarray
# arr = [
#   [1, 2, 3],
#   [2, 3, 4],
#   [5, 6, 8],
#   [10, 3, 8]
# ]
# print(sum_column(arr))
#6 - Replace number 8 with *
# def replaceNumber(array):
#     for j in range(len(array)):
#         for i in range(len(array[j])):
#             if array[j][i]==8:
#                 array[j][i]='*'
#     return array
# arr = [
#   [1, 2, 3],
#   [2, 3, 4],
#   [5, 6, 8],
#   [10, 3, 8]
# ]
# print(replaceNumber(arr))
# -------------------------------
# Ex4 Array 2D
# arr = [
#   ['banana', 'mango', 'mango', 'Jackfruit'],
#   ['orange', 'coconut', 'banana', 'papaya'],
#   ['apple', 'orange', 'mango', 'coconut'],
#   ['mango', 'coconut', 'banana', 'papaya'],
#   ['banana', 'apple', 'orange', 'coconut'],
# ]
#1 - How many fruit in list
# def count_fruite(array):
#     count=0
#     for i in range(len(array)):
#         Arr=array[i]
       
#         for j in range(len(Arr)):
#             count+=1
#     return count
# arr = [
#   ['banana', 'mango', 'mango', 'Jackfruit'],
#   ['orange', 'coconut', 'banana', 'papaya'],
#   ['apple', 'orange', 'mango', 'coconut'],
#   ['mango', 'coconut', 'banana', 'papaya'],
#   ['banana', 'apple', 'orange', 'coconut'],
# ]
# total=0
# for i in range(len(arr)):
#     total=count_fruite(arr)
# print(total)
# #2 - How many mango, orange, banana, coconut
# def find_value(array,value):
#     count=0
#     for i in range(len(array)):
#         for j in range(len(array[i])):
#             if array[i][j]==value:
#                 count+=1
#     return count
# arr = [
#   ['banana', 'mango', 'mango', 'Jackfruit'],
#   ['orange', 'coconut', 'banana', 'papaya'],
#   ['apple', 'orange', 'mango', 'coconut'],
#   ['mango', 'coconut', 'banana', 'papaya'],
#   ['banana', 'apple', 'orange', 'coconut'],
# ]
# print("Banana in list: "+str(find_value(arr,"banana")))
# print("Mango in list: "+str(find_value(arr,"mango")))
# print("Coconut in list: "+str(find_value(arr,"coconut")))
# print("Orange in list: "+str(find_value(arr,"orange")))
#3 - How many letter "o" in list
# def count_letter(Array):
#     count=0
#     for i in range(len(Array)):
#         word=Array[i]
#         for j in range(len(word)):
#             if word[j]=='o':
#                 count+=1
#     return count
# arr = [
#   ['banana', 'mango', 'mango', 'Jackfruit'],
#   ['orange', 'coconut', 'banana', 'papaya'],
#   ['apple', 'orange', 'mango', 'coconut'],
#   ['mango', 'coconut', 'banana', 'papaya'],
#   ['banana', 'apple', 'orange', 'coconut'],
# ]
# total=0
# for i in range(len(arr)):
#     total +=count_letter(arr[i])
# print(total)
#4 - How many fruits has 6 character
# arr = [
#   ['banana', 'mango', 'mango', 'Jackfruit'],
#   ['orange', 'coconut', 'banana', 'papaya'],
#   ['apple', 'orange', 'mango', 'coconut'],
#   ['mango', 'coconut', 'banana', 'papaya'],
#   ['banana', 'apple', 'orange', 'coconut'],
# ]
# count=0
# for i in range(len(arr)):
#     array=arr[i]
#     for j in range(len(array)):
#         word=array[j]
#         if len(word)==6:
#             count+=1
# print(count)
# ------------------------------
# Ex5 - Array 2D
# arr = [
#   [0, 1, 0, 0, 0],
#   [0, 0, 0, 0, 2]
#   [0, 0, 0, 0, 2],
#   [0, 0, 0, 1, 1]
# ]
#1 - How many 1 number in list
# def find_number(array):
#     count=0
#     for i in range(len(array)):
#         if array[i]==1:
#             count+=1
#     return count
# arr = [
#   [0, 1, 0, 0, 0],
#   [0, 0, 0, 0, 2],
#   [0, 0, 0, 0, 2],
#   [0, 0, 0, 1, 1]
# ]
# total=0
# for i in range(len(arr)):
#     total+=find_number(arr[i])
# print(total)
#2 - Replace 0 with $
# def replace(array):
#     for i in range(len(array)):
#         if array[i]==0:
#             array[i]='$'
#     return array
# arr = [
#   [0, 1, 0, 0, 0],
#   [0, 0, 0, 0, 2],
#   [0, 0, 0, 0, 2],
#   [0, 0, 0, 1, 1]
# ]
# Newarray=[]
# for i in range(len(arr)):
#     Newarray.append(replace(arr[i]))
# print(Newarray)
#3 - Replace 1 with 0 and replace 0 with 1
def replace_number(array):
    for i in range(len(array)):
        if array[i]==1:
            array[i]=0
        elif array[i]==0:
            array[i]=1
    return array
arr = [
  [0, 1, 0, 0, 0],
  [0, 0, 0, 0, 2],
  [0, 0, 0, 0, 2],
  [0, 0, 0, 1, 1]
]
Newarray=[]
for i in range(len(arr)):
    Newarray.append(replace_number(arr[i]))
print(Newarray)