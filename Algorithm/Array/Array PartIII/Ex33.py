# Ex1 - Object
# object = {}
# obj={}
# OBJECT={}
# #Question - Add items to object with difference price
# #     name : banana , price : 2
# #     name : coconut , price : 4
# #     name : mango , price : 3
# Array=[]
# obj['name']='Banana'
# obj['price']=2
# Array.append(obj)
# object['name']='Coconut'
# object['price']=4
# Array.append(object)
# OBJECT['name']='mango'
# OBJECT['price']=3
# Array.append(OBJECT)
# print(Array)
# -----------------------------------
# Ex2 - Dictionary
fruit_stock = {'banan': 3, 'coconut': 30, 'mango': 21}
#1 - Add new fruit: Orange with amount of 100
# fruit_stock['Orange']=100
# print(fruit_stock)
# for i in range(len(fruit_stock)):
#     fruit_stock['Orange']=100
# print(fruit_stock)
#2 - Find average all fruits
# sum=0
# Average=0
# for i in range(len(fruit_stock)):
#     sum+=i
# Average=sum/len(fruit_stock)
# print(Average)
# #3 - Find total fruit in stock
# total=0
# for fruit in fruit_stock:
#     total+=1
# print(total)
#4 - Now change fruit_stock to be input that you can input differneces fruit
# Array=eval(input())
# fruit_stock=Array
# print(fruit_stock)
# ----------------------------------

# Ex3 - Dictionary or object
# fruit_stock = [
#   {'name': 'banana', 'quality': 30},
#   {'name': 'coconut', 'quality': 10},
#   {'name': 'mango', 'quality': 20},
#   {'name': 'orange', 'quality': 42},
#   {'name': 'apple', 'quality': 25},
# ]
# #1 - Update orange quality to 100
# Quatity=0
# name=""
# for fruit in fruit_stock:
#     if fruit['name']=='orange':
#         name=fruit['name']
#         fruit['quality']=100
# print(fruit_stock)
# #2 - Count the quality of fruit in stock
# count=0
# for fruit in fruit_stock:
#     count+=fruit['quality']
# print(count)
# #3 - Which fruit have less in stock
# min=fruit_stock[0]['quality']
# name=""
# for fruit in fruit_stock:
#     if fruit['quality']<min:
#         min=fruit['quality']
#         name=fruit['name']
# print(name)
#4 - Which fruit has the most in stock
# max=fruit_stock[0]['quality']
# Name=""
# for fruit in fruit_stock:
#     if fruit['quality']>=max:
#         max=fruit['quality']
#         Name=fruit['name']
# print(Name)
# ---------------------------------
# Ex4 - Dictionary or object
fruit_stock = [
  {'name': 'banana', 'quality': 1},
  {'name': 'coconut', 'quality': 8},
  {'name': 'mango', 'quality': 10},
  {'name': 'orange', 'quality': 0},
  {'name': 'apple', 'quality': 5},
]

# #1 - Display fruit that has in stock
NameFruit=""
maxfruit=fruit_stock[0]['quality']
for fruit in fruit_stock:
    if fruit['quality']>maxfruit:
        maxfruit=fruit['quality']
        NameFruit+=fruit['name']
print(NameFruit)
#2 - Display fruit that has more than 5 in stock
for fruit in fruit_stock:
    if fruit['quality']<5:
        print(fruit['name'])
#3 - Increase quality of fruit that has less than 10 in stock to 20
