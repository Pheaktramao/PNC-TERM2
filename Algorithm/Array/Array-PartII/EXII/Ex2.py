# Ex2 - basic 2
arr = [2, 3, 4, 3, 2, 5, 3, 2, 5]

#1 - Square odd number in list
# for i in range(len(arr)):
#     if arr[i]%2==1:
#         arr[i]*=arr[i]
# print(arr)
#2 - Filter list with dupplicate values
arr.sort()
array=[]
for i in range(len(arr)):
    if arr[i]!=arr[i-1]:
        array.append(arr[i])
print(array)
#    output: [2, 3, 4, 5]