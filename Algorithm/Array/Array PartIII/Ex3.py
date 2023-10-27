# Ex3 - Array 2D#1 - sum in column
# [12, 11, 15]
arr2D = [
  [1, 2, 3],
  [3, 5, 9],
  [8, 4, 3]
]

m=0
sumarr=[]
while m<len(arr2D):
    sum=0
    for i in range(len(arr2D)):
        n=arr2D[i]
        for j in range(len(n)):
            if j==m:
                sum+=n[j]
    sumarr.append(sum)
    m+=1
print(sumarr)
sum=0
newArr=[]
for i in range(len(arr2D)):
    arr=arr2D[i]
    for j in range(len(arr)):
        sum+=arr[j]
    newArr.append(sum)
    sum=0
print(newArr)
#2 - sum first column 
sum=0
for i in range(len(arr2D)):
    number=arr2D[i]
    sum+=number[0]
print("result: "+ str(sum))
# result: 12
# 3 - sum last column
sum=0
for i in range(len(arr2D)):
    number=arr2D[i]
    sum+=number[-1]
print("result: "+ str(sum))
result: 15
#4 How many row and column in this array 2D
sumcul=0
for i in range(len(arr2D)):
    n=arr2D[i]
    sumrow=0
    for j in range(len(n)):
        sumrow+=1
    sumcul+=1
print(str(sumrow)+" rows " + str(sumcul)+" columns")
# result: 3 rows 3 columns
#5 Find index of 9
number=""
index=0
for i in range(len(arr2D)):
    number=arr2D[i]
    for j in range(len(number)):
        if number[j]==9:
            index=j
print("result: "+str(index))
# result: 2