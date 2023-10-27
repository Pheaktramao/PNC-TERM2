def NumberOfCompare(array):
    count=0
    if len(array)>0:
        for i in range(len(array)-1):
            if int(array[i])<int(array[i+1]):
                count+=1
        return count
    else:
        return 0
integer=eval(input())
print(NumberOfCompare(integer))