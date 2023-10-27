def max(n1, n2):
    result=0
    if n1>n2:
        result=n1
    else:
        result=n2
    return result
n1=int(input())
n2=int(input())
print("Maximum is:", max(n1,n2))