n=int(input())
result=""
mode=input()
if n>=1 and n<=10 and mode=="inside":
    result=True
elif n<1 or n>10 and mode=="outside":
    result=True
else:
    result=False
print(result)