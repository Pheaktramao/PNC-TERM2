# Ex3:
# number of array: 2
# > [3, 2]
# > [1, 3, 4]
# def average(array):
#     sum=0
#     aver=0
#     for i in range(len(array)):
#         sum+=array[i]
#     aver=sum/len(array)
#     return aver
# NumberOfArray=int(input())
# total=0
# for i in range(NumberOfArray):
#     array=eval(input())
#     result=average(array)
#     print(result)
# output:
# 2.5
# 2.66666666
# -----------------
# Ex4:
# number of array: 2
# > [3, 2]
# > [1, 3, 4]

# output:
# [9, 4]
# [1, 9, 16]
def Square(array):
    NewList=[]
    for i in range(len(array)):
        NewList.append(array[i]*array[i])
    return NewList
Number=int(input())
for i in range(Number):
    array=eval(input())
    Square(array)
    print(Square(array))