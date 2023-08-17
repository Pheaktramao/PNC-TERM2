# def sum():
#     Number=int(input("Number of values:"))
#     result=0
#     for i in range(Number):
#         value=int(input("value:"))
#         result+=value
#     return result
# print("The sum is:", sum())

def sum(n1, n2):
    return n1+n2
Numberoftime=int(input("Number of time:"))
for i in range(Numberoftime):
    result=0
    number=int(input("value"+str(i+1)+":"))
    if i==0:
        previousValue=number
    else:
        previousValue=sum(previousValue,number)
    result=previousValue
print(result)