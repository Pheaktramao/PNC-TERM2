# Ex1 - String
text = "banana"
#1 - How many letter in string
count=0
for i in range(len(text)):
    count+=1
print(count)
#2 - How many letter "A" in string
countA=0
for i in range(len(text)):
    if text[i]=="a":
        countA+=1
print(countA)
# 3 - Reverse string
result=""
for i in range(len(text)):
    result+=text[-1-i]
print(result)
#4 - Convert all letter to uppercase except letter "A"
result=""
for i in range(len(text)):
    if text[i]!="a":
        result+=text[i].upper()
    else:
        result+=text[i]
print(result)

# -----------------------
# Ex2 - Array
arr = [1000, 200, 404, 500, 10]
#1 - How many degit of each item
newarr=[]
for i in range(len(arr)):
    number=str(arr[i])
    n=len(number)
    newarr.append(n)
print(newarr)
[4, 3, 3, 3, 2]
#2 - Remove 404 from list
index=0
for i in range(len(arr)):
    if arr[i]==404:
        index=i
arr.pop(index)
print(arr)
#3 - Reverse array
# [10, 500, 404, 200, 1000]
result=""
newarr=[]
for i in range(len(arr)):
    result+=str(arr[-1-i])
    newarr.append(result)
    result=""
print(newarr)
#4 - Sum only number with last degit is 0
number=''
sum=0
for i in range(len(arr)):
    number=str(arr[i])
    if number[len(number)-1]=="0":
        sum+=int(number)
print(sum)
# result: 1710