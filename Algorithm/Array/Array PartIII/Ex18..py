# Ex2 - Array
arr = [1010, 55, 993, 2]
#1 - How many degit of each number
Newlist=[]
for i in range(len(arr)):
    array=str(arr[i])
    n=0
    for i in range(len(array)):
        n+=1
    Newlist.append(n)
print(Newlist)
[4, 2, 3, 1]
# #2 - Reverse array
Newlist=[]
for i in range(len(arr)):
    Newlist.append(arr[-1-i])
print(Newlist)
#3 - Sum only number > 2 degit
Newlist=[]
for i in range(len(arr)):
    array=str(arr[i])
    sum=0
    if len(array)>2:
        for i in range(len(array)):
            sum+=int(array[i])
    Newlist.append(sum)
print(Newlist)