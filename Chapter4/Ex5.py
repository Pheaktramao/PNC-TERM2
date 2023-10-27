# Ex4 - Array string
arr = ['rady','ronan','him','yon','mengheang']
#1 - How many letter "A" and "O" in list
word=""
CountA=0
CountO=0
for i in range(len(arr)):
    word=arr[i]
    for j in range(len(word)):
        if word[j]=='a':
            CountA+=1
        elif word[j]=='o':
            CountO+=1
print("Letter A : "+ str(CountA)+"\n"+"Letter O : "+ str(CountO))
#2 - Reverse array
NewArr=[]
for i in range(len(arr)):
    NewArr.append(arr[-1-i])
print(NewArr)
#3 - Reverse text in array
word=""
NewArr=[]
for i in range(len(arr)):
    word=arr[i]
    result=""
    for j in range(len(word)):
        result+=word[-1-j]
    NewArr.append(result)
print(NewArr)
#4 - count letter in array: [4, 4, 3, 3, 9]
NewArr=[]
for i in range(len(arr)):
    array=arr[i]
    count=0
    for j in range(len(array)):
        count+=1
    NewArr.append(count)
print(NewArr)
#5 - create array 2D with string in list
Arr2D=[]
for i in range(len(arr)):
    array=arr[i]
    newArr=[]
    for j in range(len(array)):
        newArr.append(array[j])
    Arr2D.append(newArr)
print(Arr2D)
# [['r','a','d','y'],....]