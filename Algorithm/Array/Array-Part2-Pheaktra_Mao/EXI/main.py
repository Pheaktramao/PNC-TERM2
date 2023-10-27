# Ex1 - Basic array

# array = [1, 4, 5, 2, 9, 1, 6, 3, 2]

#1 - How many value in array
# print(len(array))
#2 - Sum all value in array
# result=0
# for i in range(len(array)):
#     result+=array[i]
# print(result)
#3 - Count even / odd number in array
# CountEven=0
# CounOdd=0
# for i in range(len(array)):
#     if array[i]%2==0:
#         CountEven+=1
#     else:
#         CounOdd+=1
# print(str(CountEven)+"\n"+str(CounOdd))
#4 - Find first index of 2
# isfirstOfTwo=False
# index=0
# i=0
# while i<len(array) and not isfirstOfTwo:
#     if array[i]==2:
#         index=i
#         isfirstOfTwo=True
#     i+=1
# print(index)
#5 - Replace number 1 by 88 and 2 by 99
# for i in range(len(array)):
#     if array[i]==1:
#         array[i]=88
#     elif array[i]==2:
#         array[i]=99
# print(array)
#6 - If value is 1 add 3 more and if value greater than 2 minus 1
# add=3
# minus=1
# for i in range(len(array)):
#     if array[i]==1:
#         array[i]+=add
#     elif array[i]>2:
#         array[i]-=minus
# print(array)

