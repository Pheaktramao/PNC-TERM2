# Ex4 - Array pop() function

array = [1, 2, 3, 5, 7, 9, 7, 4, 8]

#1 - Remove number 3 from list
arr=[]
for i in range(len(array)):
    arr.append(array[i])
arr.pop(2)
print(arr)
#2 - Remove first 7 from list
arr=[]
for i in range(len(array)):
    if array[i]!=7:
        arr.append(array[i])
print(arr)
#3 - Remove only odd number from list
arr=[]
for i in range(len(array)):
    if array[i]%2==0:
        arr.append(array[i])
print(arr)
#4 - Remove only value < 5 from list
arr=[]
for i in range(len(array)):
    if array[i]>5:
        arr.append(array[i])
print(arr)