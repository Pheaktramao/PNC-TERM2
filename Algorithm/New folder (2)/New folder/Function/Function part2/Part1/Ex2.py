def multiply(n1,n2):
    return n1*n2
def productFromTo(start,end):
    total=1
    while start<=end:
        total=multiply(total,start)
        start+=1
    return total
start=int(input())
end=int(input())
print("The result is ", productFromTo(start,end))