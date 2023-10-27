# Ex7:
# Count number 10 in list of array 2D
Array2D=eval(input("Enter array"))
for i in range(len(Array2D)):
    array=Array2D[i]
    count=0
    for j in range(len(array)):
        if array[i]==10:
            count+=1
print("number 10 is " +str(count))
# Test case 1:

# Enter array: [[1, 2, 4, 5], [14, 16, 10, 11], [10, 9, 10, 10]]
# ouput
# number 10 is 4

# Test case 2:
# Enter array: [[1, 2, 4, 5], [14, 16, 8, 11], [8, 9, 8, 8]]
# ouput
# number 10 is 0