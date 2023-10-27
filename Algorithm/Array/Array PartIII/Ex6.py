# Ex1:
# number of array: 3
# > [3, 3]
# > [1, 3, 4]
# > [4, 5, 9, 1]
# def sum(array):
#     # array=eval(input())
#     total=0
#     for i in range(len(array)):
#         total+=array[i]
#     return total
# NumberOfArray=int(input())
# sumarr=""
# for i in range(NumberOfArray):
#     array2D=eval(input())
#     result=sum(array2D)
#     sumarr+=str(result)+"\n"
# print(sumarr)
# output:
# 6
# 8
# 19
# ———————————————-
# Ex2:
# number of array: 2
# > [3, 2]
# > [1, 3, 4]
def ReverseArray(array):
    lastIndex=len(array)-1
    NewArray=[]
    for i in range(len(array)):
        NewArray.append(array[lastIndex-i])
    return NewArray
NumberOfArray=int(input())
for i in range(NumberOfArray):
    array2D=eval(input())
    ReverseArray(array2D)
    print(ReverseArray(array2D))
# output:
# [2, 3]
# [4, 3, 1]
