# Ex2 - Array number
#1 - Remove duplicate value in list by create new list
def CheckValue(value,list):
    isFound=False
    for i in range(len(list)):
        if value==list[i]:
            isFound=True
    return isFound
arr = [1, 9, 7, 7, 8, 3, 5,12, 1, 10]
list=[]
for i in range(len(arr)):
    if not CheckValue(arr[i],list):
        list.append(arr[i])
print(list)
#2 - Remove 8 from list
#3 - Find average of this list
sum=0
average=0
for i in range(len(arr)):
    sum+=arr[i]
average=sum/len(arr)
print(average)
#4 - Create new list with letter "A" following number in array
newarr=[]
result=""
for i in range(len(arr)):
    n=arr[i]
    for j in range (n):
        result+="A"
    newarr.append(result)
    result=""
print(newarr)
# ['A','AAAAAAAAA','AAAAAAA', 'AAAAAAA',......]
#5 - Sum only duplicate value
def checkValue(value,arr):
    isTrue=True
    isRun=False
    j=0
    while j<len(arr) and not isRun:
        if value==arr[j] and i!=j:
            isTrue=True
            isRun=True
        else:
            isTrue=False
        j+=1
    return isTrue
arr = [1, 9, 7, 7, 8, 3, 5,12, 1, 10]
newarr=[]
for i in range(len(arr)):
    number=arr[i]
    if checkValue(number,arr):
        arr[i]+=arr[i]
        newarr.append(arr[i])
print(newarr)
[2,14]
#6 - Do NOT create new array remove all duplicate value
#7 - Replace all duplicate value with *
def checkValue(value,list):
    isTrue=False
    for i in range(len(list)):
        if value==list[i]:
            isTrue=True
    return isTrue
arr = [1, 9, 7, 7, 8, 3, 5,12, 1, 10]
list=[]
for i in range(len(arr)):
    if not checkValue(arr[i],list):
        list.append(arr[i])
    else:
        arr[i]='*'
        list.append(arr[i])
print(list)
#8 - Add value to 10 if value < 10
arr = [1, 9, 7, 7, 8, 3, 5,12, 1, 10]
Newarray=[]
for i in range(len(arr)):
    if arr[i]<10:
        arr[i]=10
        Newarray.append(arr[i])
print(Newarray)
# 9 - Add if value <= 5 and replace if value > 5 to make list store only 5 number
arr = [1, 9, 7, 7, 8, 3, 5,12, 1, 10]
Newarray=[]
for i in range(len(arr)):
    if arr[i]<=5:
        arr[i]=5
    else:
        arr[i]=5
    Newarray.append(arr[i])
print(Newarray)
[5, 5, 5, 5, 5, 5, 5, 5,5]
# ------------------------------------------------------
