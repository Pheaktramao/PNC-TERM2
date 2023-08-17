def comparisonNumber(n1,n2):
    result=""
    if n1>n2:
        result=str(n1) + " is greater than " + str(n2)
    else:
        result=str(n1) + " is less than " + str(n2)
    return result
n1=int(input())
n2=int(input())
print(comparisonNumber(n1,n2))