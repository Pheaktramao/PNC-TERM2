# food={
#     "Name":"baychar",
#     "Price":10000
# }
# for key in food:
#     print(key)
# for key in food:
    # print(Name)

# studentRecord = [
#     {"studentName":"Seyla","class":"wep-a","algorithm":98,"html":90},
#     {"studentName":"seyha","class":" wep-b","algorithm":80,"html":90},
#     {"studentName":"Villa","class":"wep-a","algorithm":96,"html":92},
#     {"studentName":"mengheang","class":"wep-a","algorithm":66,"html":54},
#     {"studentName":"meng","class":"wep-a","algorithm":90,"html":98},
#     {"studentName":"lyly","class":"wep-a","algorithm":78,"html":60}
# ]
# count=0
# score=0
# for student in studentRecord:
#         if student["class"]=="wep-a":
#             count+=1
#             score+=student['algorithm']
# print(score/count)

# def reverse_word(word):
#     result=""
#     for i in range(len(word)):
#         result+=word[-1-i]
#     return result
# arr=eval(input("Enter Array: "))
# newArr=[]
# for i in range(len(arr)):
#     newArr.append(reverse_word(arr[i]))
# print(newArr)


# def reverse_word(word):
#     result=""
#     for i in range(len(word)):
#         result+=word[-1-i]
#     return result
# Array=eval(input("ENTER: "))
# newArr=[]
# for i in range(len(Array)):
#     newArr.append(reverse_word(arr[-1-i]))
# print(newArr)

# array=eval(input())
# columns=len(array[0])
# row= len(array)
# for i in range(row):
#     for j in range(columns):
#         print(array[i][j])

# Ex3 - Array 2D
arr2D = [
  [1, 2, 3,10,4],
  [3, 5, 9,5,6],
  [8, 4, 3,6,8]
]
# #1 - sum in column
# [12, 11, 15]
# newArr=[]
# row=len(arr2D)
# columns=len(arr2D[0])
# sum=0
# for i in range(columns):
#     for j in range(row):
#         sum+=arr2D[j][i]
#     newArr.append(sum)
#     sum=0
# print(newArr)
# #2 - sum first column 
# result: 12
# columns=len(arr2D[0])
# row=len(arr2D)
# for i in range(columns):
#     if i==0:
#         for j in range(row):
#             sum+=arr2D[j][i]
# print(sum)
# #3 - sum last column
sum=0
columns=len(arr2D[0])
row=len(arr2D)
for i in range(columns):
    if i==columns-1:
        for j in range(row):
            sum+=arr2D[j][i]
print(sum)
# result: 15
# #4 How many row and column in this array 2D
# result: 3 rows 3 columns
columns=len(arr2D[0])
row=len(arr2D)
print(str(row) +" rows "+ str(columns)+" columns")
# #5 Find index of 9
# result: 2