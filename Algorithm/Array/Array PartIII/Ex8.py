# Ex5:
# Find index of number in list (each value is unique)
# Test case 1:
def FindNumber(Value,list):
    isTrue=True
    result=""
    for i in range(len(list)):
        if list[i]==Value:
            result=str(list[i])+" at position " +str(i)
        else:
            result=str(Value)+" Not found in list "
    return result
list=eval(input("ENTER ARRAY: "))
Value=int(input("ENTER NUMBER: "))
print(FindNumber(Value,list))
# Enter array: [1,2,4,10,9]
# Enter number: 10
# ouput
# 10 at position 3

# Test case 2:

# Enter array: [5,4,10,3]
# Enter number: 5
# ouput
# 5 at position 0

# Test case 3:

# Enter array: [5,4,10,3]
# Enter number: 8
# ouput
# 8 not found in list