# Ex1 - Create new object
# Object container: id, name, quality, price
# number of object: 3
# > {'id': 1, 'name': 'Coconut', 'quality': 3, 'price': 100}
# > {'id': 2, 'name': 'Banana', 'quality': 10, 'price': 150}
# > {'id': 3, 'name': 'Mango', 'quality': 23, 'price': 70}
# output:
#   [
#     {'id': 1, 'name': 'Coconut', 'quality': 3, 'price': 100},
#     {'id': 2, 'name': 'Banana', 'quality': 10, 'price': 150},
#     {'id': 3, 'name': 'Mango', 'quality': 23, 'price': 70}
# #   ]
# number_of_object=int(input("number of object: "))
# Fruit=[]
# for i in range (number_of_object):
#     number={}
#     number['id']=int(input('id '))
#     number['name']=input('name ')
#     number['quality']=int(input('quality '))
#     number['price']=int(input('price '))
#     Fruit.append(number)
# print(Fruit)
# ---------------------------
# Ex2 - Dictionary or object
fruit_stock = [
  {'id': 1, 'name': 'Coconut', 'quality': 3, 'price': 4000},
  {'id': 2, 'name': 'Banana', 'quality': 10, 'price': 2500},
  {'id': 3, 'name': 'Mango', 'quality': 23, 'price': 2000}
]

#1 - How many fruit in stock
# count=0
# for i in range(len(fruit_stock)):
#     count+=1
# print(count)
#2 - if 1 mango = 2000៛ how much we can get money after sell all mango
# multipy=1
# for fruit in fruit_stock:
#     if fruit['name']=='Mango':
#         multipy=fruit['quality']*fruit['price']
# print(multipy)
#3 - Following price how much money we can get after sell all fruit from stock
multipy=1
for fruit in fruit_stock:
    multipy+=fruit['quality']*fruit['price']
print(multipy)
# ------------------