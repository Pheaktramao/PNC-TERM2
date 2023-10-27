# # Ex8
# # Search students from list of array 2D
# def findValue(array,Value):
#     count=0
#     for i in range (len(array)):
#         Arr=array[i]
#         for j in range(len(Arr)):
#             if Arr[j]==Value:
#                 count+=1
#     return count
# students = [
#   ['bopha','2024A','kandal'],
#   ['romdule','2024C','kompot'],
#   ['kaka','2024C','Rathanakiri'],
#   ['chompey','2024B','Siem Riep'],
#   ['chompa','2024B','Battambang']
# ]
# # value=input()
# print("Student from class A "+str(findValue(students,"2024A")))
# print("Student from class B "+str(findValue(students,"2024B")))
# print("Student from class C "+str(findValue(students,"2024C")))
# #1 - how many students from class A? B? and C?
# #2 - Where kaka come from?
# for i in range(len(students)):
#     array=students[i]
#     isstop=False
#     for j in range(len(array)):
#         if array[j]=="kaka" and not isstop:
#             array=array[2]
#         isstop=True
# print("KaKa come from "+str(array[2]))
# #3 - Which class Chompey study?
# for i in range(len(students)):
#     array=students[i]
#     isstop=False
#     for j in range(len(array)):
#         if array[j]=="campey" and not isstop:
#             array=array[1]
#         isstop=True
# print("Champey from class "+str(array[1]))
# #4 - Replace Chompa province to Prey Veng
# for i in range(len(students)):
#     array=students[i]
#     for j in range(len(array)):
#         if array[j]=='Champa':
#             array[2]='Prey Veng'

# Ex9
# From list of array 2D
# fruits = [
#   ['banana','coconut','mango'],
#   ['jackfruit','banana','mango'],
#   ['papaya','apple','orange'],
#   ['mango','orange','Mango'],
#   ['banana','mango','orange']
# ]
#1 - How many letter "A" from array 2D (function)
# def findLetter(array):
#     count=0
#     for i in range(len(array)):
#         if array[i]=='a':
#             count+=1
#     return count
# fruits = [
#   ['banana','coconut','mango'],
#   ['jackfruit','banana','mango'],
#   ['papaya','apple','orange'],
#   ['mango','orange','Mango'],
#   ['banana','mango','orange']
# ]
# result=''
# total=0
# sum=0
# for i in range(len(fruits)):
#     arr=fruits[i]
#     for j in range(len(arr)):
#         result=arr[j]
#         total=findLetter(result)
#         sum+=total
# print("Letter A is list are "+str(sum))
# 2 - How many banana in list (function)
def findBanana(array):
    count=0
    for i in range(len(array)):
        if array[i]=='banana':
            count+=1
    return count
fruits = [
  ['banana','coconut','mango'],
  ['jackfruit','banana','mango'],
  ['papaya','apple','orange'],
  ['mango','orange','Mango'],
  ['banana','mango','orange']
]
result=0
for i in range(len(fruits)):
    fruit=fruits[i]
    sum=0
    for j in range(len(fruit)):
        result=findBanana(fruit)
        sum+=result
print("banana in list are: "+str(sum))
# #3 - How many mango in list (function)
def FindFruits(array):
    count=0
    for i in range(len(array)):
        if array[i]=='mango' or array[i]=='Mango':
            count+=1
    return count
fruits = [
  ['banana','coconut','mango'],
  ['jackfruit','banana','mango'],
  ['papaya','apple','orange'],
  ['mango','orange','Mango'],
  ['banana','mango','orange']
]
total=0
for i in range(len(fruits)):
    fruit=fruits[i]
    counter=0
    for j in range(len(fruit)):
        total=FindFruits(fruit)
        counter+=total
print("mango in list are: "+str(counter))
#5 - Replace mango by # sign (function)
fruits = [
  ['banana','coconut','mango'],
  ['jackfruit','banana','mango'],
  ['papaya','apple','orange'],
  ['mango','orange','Mango'],
  ['banana','mango','orange']
]
for fruitlist in fruits:
    for i in range(len(fruitlist)):
        if fruitlist[i].lower()=='mango':
            fruitlist[i]="#"
print(fruits)
        
# def countfruit(fruits, fruit_name):
#     count=0
#     for fruit in fruits:
#         if fruit.lower()==fruit_name.lower():
#             count+=1
#     return count
# fruits = [
#   ['banana','coconut','mango'],
#   ['jackfruit','banana','mango'],
#   ['papaya','apple','orange'],
#   ['mango','orange','Mango'],
#   ['banana','mango','orange']
# ]
# counter=0
# for fruitlist in fruits:
#     counter+=countfruit(fruitlist,'mango')
# print(counter)