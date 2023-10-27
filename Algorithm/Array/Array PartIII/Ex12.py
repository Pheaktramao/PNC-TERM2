# Ex10
# From list of array 2D
# numbers = [
#   [1,3,4, 4],
#   [3, 4, 0, 4]
#   [5, 6, 9, 0]
#   [4, 5, 9, 7]
# ]
#1 - How many number 4 from array 2D (function)
# def findenumber(array):
#     count=0
#     for i in range(len(array)):
#         if array[i]==4:
#             count+=1
#     return count
# numbers = [
#   [1,3,4, 4],
#   [3, 4, 0, 4],
#   [5, 6, 9, 0],
#   [4, 5, 9, 7]
# ]
# n=0
# for i in range(len(numbers)):
#     arr=numbers[i]
#     counter=0
#     for j in range(len(arr)):
#         n=findenumber(arr)
#         counter+=n
# print(counter)
# def findNumber(numbers):
#   count=0
#   for i in range(len(numbers)):
#       array=numbers[i]
#       for j in range(len(array)):
#           if array[j]==4:
#               count+=1
#   return count
# numbers = [
#   [1,3,4, 4],
#   [3, 4, 0, 4],
#   [5, 6, 9, 0],
#   [4, 5, 9, 7]
# ]
# print(findNumber(numbers))
#2 - Sum each list of array in array 2D (function)
# def sumarray(array):
#     count=0
#     for i in range(len(array)):
#         count+=array[i]
#     return count
# numbers = [
#   [1,3,4, 4],
#   [3, 4, 0, 4],
#   [5, 6, 9, 0],
#   [4, 5, 9, 7]
# ]
# Newarray=[]
# total=0
# for i in range(len(numbers)):
#     total=sumarray(numbers)
#     Newarray.append(total)
# print(Newarray)
# output: [12, 11, 20, 25]
#3 - Sum only number 4 in list 
numbers = [
  [1,3,4, 4],
  [3, 4, 0, 4],
  [5, 6, 9, 0],
  [4, 5, 9, 7]
]
sum=0
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        if numbers[j][i]==4:
            sum+=numbers[j][i]
print(sum)
#4 - Replace number 0 with 99 (function)
numbers = [
  [1,3,4, 4],
  [3, 4, 0, 4],
  [5, 6, 9, 0],
  [4, 5, 9, 7]
]
for n in range(len(numbers)):
    for i in range(len(n)):
        if n[i]==0:
            n[i]=99
print(numbers)
def replaceNumber(array):
    NewArray=[]
    for i in range(len(array)):
        if array[i]==0:
            array[i]=99
    return array[i]
#5 - where find index of 7 in list 
# output: [3][3]