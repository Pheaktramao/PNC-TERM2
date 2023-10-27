array=eval(input())
sum=0
arr=[]
isTrue=True
for i in range(len(array)):
    sum+=array[i]
    if sum<200:
        arr.append(array[i])
    elif sum>=200:
        isTrue=False
if sum>=200:
    print(arr)
else:
    print([])