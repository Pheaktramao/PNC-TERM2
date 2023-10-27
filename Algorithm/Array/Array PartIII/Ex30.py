# Ex7 - Array 2D
# input: [3,4, 5, 1]
# ouput: 
# [
#   [1, 2, 3],
#   [1, 2, 3, 4],
#   [1, 2, 3, 4, 5],
#   [1]
# ]
def make_array2D(array):
    list=[]
    for i in range(array):
        list.append(i+1)
    return list
Arr=eval(input())
newArr=[]
for i in range(len(Arr)):
    newArr.append(make_array2D(Arr[i]))
print(newArr)