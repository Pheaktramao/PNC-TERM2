# Ex5 - Array insert() & append()

array = [1, 2, 5]

#1 - Add number 7 to last index of array
arr=[]
for i in range(len(array)):
    arr.append(array[i])
arr.append(7)
print(arr)
#2 - Add number 8 before index 0 in list
array.insert(1,8)
print(array)
#3 - Add number 9 after index 1 in list
array.insert(2,9)
print(array)