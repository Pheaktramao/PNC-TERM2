# Ex1 - Loop
#1 - loop to display from 10 to 1 (while)
# i=0
# while i<11:
#     if i>0:
#         print(11-i)
#     i+=1
#2 - loop to display only number between 10 to 20 (while)
# i=0
# while i<21:
#     if i>=10 and i<=21:
#         print(i)
#     i+=1
#3 - Loop to display from 50 to 40 (while)
# i=50
# while i>=40:
#     print(i)
#     i-=1

# Ex2 - String
text = "125345645"
#1 - Sum all number (while)
# i=0
# sum=0
# while i<len(text):
#     sum+=int(text[i])
#     i+=1
# print(sum)
#2 - Find first index of 5 (while)
# i=0
# index=0
# isStop=False
# while i<len(text) and not isStop:
#     if text[i]=="5":
#         index=i 
#         isStop=True
#     i+=1
# print(index)
#3 - Find average all number (while)
# i=0
# sum=0
# average=0
# while i<len(text):
#     sum+=int(text[i])
#     i+=1
# average=sum/len(text)
# print(average)

# Ex3 - String
text = "10 12 4 11"
#1 - Sum all number seperate by space (while)
# i=0
# sum=0
# n=''
# while i<len(text):
#     if text[i]!=" ":
#         n+=text[i]
#     else:
#         sum+=int(n)
#         n=''
#     i+=1
# sum+=int(n)
# print(sum)
#2 - find average of that number (while)
i=0
average=0
sum=0
n=''
while i<len(text):
    if text[i]!=" ":
        n+=text[i]
    else:
        sum+=int(n)
        n=''
    i+=1
sum+=int(n)
average=sum/len(text)
print(average)
#3 - how many number greater than 10 (while)
# count=0
# i=0
# while i<len(text):
#     if text[i]>"10":
#         count+=1
#     i+=1
# print(count)
# Ex4 - Array (using while loop only)
arr = [1, 3, 5, 8, 9, 0, 5]
#1 - find index of 9
# index=0
# isStop=False
# i=0
# while i<len(arr) and not isStop:
#     if arr[i]==9:
#         index=i
#         isStop=True
#     i+=1
# print(index)
#2 - find last index of 5
i=0
index=0
while i<len(arr):
    if arr[i]==5:
        index=i
    i+=1
print(index)
#3 - find first index of 5
i=0
index=0
isFirst=False
while i<len(arr) and not isFirst:
    if arr[i]==5:
        index=i
        isFirst=True
    i+=1
print(index)
#4 - sum only odd number
i=0
sum=0
while i<len(arr):
    if arr[i]%2==1:
        sum+=arr[i]
    i+=1
print(sum)
#5 - remove 8 from list
i=0
index=0
while i<len(arr):
    if arr[i]==8:
        index=i
        print(index)
    i+=1
arr.pop(index)
print(arr)
#6 - replace 0 by 33
i=0
while i<len(arr):
    if arr[i]==0:
        arr[i]=33
    i+=1
print(arr)