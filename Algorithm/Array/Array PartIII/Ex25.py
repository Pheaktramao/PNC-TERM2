# Ex2 - Array
# Find index
# input1: [3, 3, 4, 5, 6, 6]
# input2: [3, 4, 6]
# ouput: {3: 0, 3: 1, 4: 2, 6:4, 6:5}
def find_index(array,value):
    index=None
    for i in range(len(array)):
        if array[i]==value:
            index=i
    return index
Array=eval(input("ENTER ARRAY:"))
ArrFind=eval(input("ENTER ARRAY:"))
newArr={}
for i in range(len(ArrFind)):
    newArr[ArrFind[i]]=(find_index(Array,ArrFind[i]))
print(newArr)