# Ex2 - Array 2D
arr2D = [
  [1, 2, 3],
  [3, 5, 9],
  [8, 4, 3]
]
# sum=0
# for i in range(len(arr2D)):
#     arr=arr2D[i]
#     sum=0
#     for j in range(len(arr)):
#         sum+=arr[j]
#     arr2D[i]=sum
# print(arr2D)
#1 - Sum each array
# [6, 17, 15]
#2 - Select only odd number
NewArray=[]
Number=""
for i in range(len(arr2D)):
    Number=arr2D[i]
    for j in range(len(Number)):
        if Number[j]%2 !=0:
            NewArray.append(Number[j])
print(NewArray)
# [1, 3, 3, 5, 9, 3]
#3 - Replace all even number with 168
# [
#   [168, 2, 168],
#   [168, 168, 168],
#   [8, 4, 168]
# ]
NewArray=[]
Number=""
for i in range(len(arr2D)):
    Number=arr2D[i]
    for j in range(len(Number)):
        if Number[j]%2!=0:
            Number[j]=168
    print(Number)