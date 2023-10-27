# Ex2 - Basic array

array = [1, 4, 5, 2, 9, 1, 6, 3, 2]

#1 - Find average of value in array
# average=0
# sum=0
# number=len(array)
# for i in range(len(array)):
#     sum+=array[i]
# average=sum/number
# print(average)
#2 - Find max / min value in array
# max=array[0]
# min=array[0]
# for i in range(len(array)):
#     if array[i]>max:
#         max=array[i]
#     elif array[i]<min:
#         min=array[i]
# print(str(min)+"\n"+str(max))
#3 - If odd value add 1 and if even value minus 1
# Odd=1
# Even=1
# for i in range(len(array)):
#     if array[i]%2==0:
#         array[i]-=Even
#     else:
#         array[i]+=Odd
# print(array)
#4 - How many number < 5 in array
# result=0
# for i in range(len(array)):
#     if array[i]<5:
#         result+=1
# print(result)
#5 - Square value of array
# for i in range(len(array)):
#     array[i]*=array[i]
# print(array)