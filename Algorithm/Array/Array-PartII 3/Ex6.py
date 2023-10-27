# Ex7 - Array (while only)
arr = [1024, 1010, 2024, 123454]

#1 - How many degit each item
# i=0
# NewArray=[]
# while i<len(arr):
#     number=str(arr[i])
#     n=len(number)
#     NewArray.append(n)
#     i+=1
# print(NewArray)
[4, 4, 4, 6]
#2 - Sum each number in each value together (1 + 0 + 2 + 4)
# i=0
# number=''
# NewArray=[]
# while i<len(arr):
#     number=str(arr[i])
#     j=0
#     sum=0
#     while j<len(number):
#         sum+=int(number[j])
#         j+=1
#     NewArray.append(sum)
#     i+=1
# print(NewArray)
[7, 2, 8, 19]
#3 - Sum only last degit number on each item (4 + 0 + 4 + 4)
i=0
sum=0
while i<len(arr):
    number=str(arr[i])
    index=number[len(arr)-1]
    sum+=int(index)
    i+=1
print(sum)
sum = 12