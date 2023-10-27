def sumBetweenNumberTwo(array):
    sum=0
    i=0
    isTwo=False
    while i<len(array):
        if int(array[i])==2:
            isTwo=True
        elif isTwo:
            if int(array[i])!=2:
                sum+=int(array[i])
        elif int(array[i])!=2:
            sum+=int(array[i])
        else:
            if int(array[i])==2:
                isTwo= False
        i+=1
    return sum
number=eval(input())
print(sumBetweenNumberTwo(number))