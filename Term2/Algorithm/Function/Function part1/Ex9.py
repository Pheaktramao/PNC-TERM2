def comparisonNumber(n1,n2):
    result=""
    if n1<n2:
        result=str(n2) + " is greater than " + str(n1)
    else:
        result=str(n2) + " is less than " + str(n1)
    return result
n1=int(input())
n2=int(input())
print(comparisonNumber(n1,n2))