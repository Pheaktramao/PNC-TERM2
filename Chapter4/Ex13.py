# Ex3 - Dictionary or object
fruit_stock = [
  {'id': 1, 'name': 'Coconut', 'quality': 3, 'price': 4000},
  {'id': 2, 'name': 'Banana', 'quality': 0, 'price': 2500},
  {'id': 3, 'name': 'Mango', 'quality': 23, 'price': 2000},
  {'id': 4, 'name': 'Orange', 'quality': 0, 'price': 5000},
  {'id': 5, 'name': 'Apple', 'quality': 5, 'price': 3000},
  {'id': 6, 'name': 'Jackfruit', 'quality': 13, 'price': 6000},
]
#1 - How many fruit have in stock
sum=0
for i in range(len(fruit_stock)):
    sum+=1
print(sum)
#2 - How many fruit no more in stock
FruitQuality=fruit_stock[0]['quality']
Name=""
for fruit in fruit_stock:
    if fruit['quality']==0:
        FruitQuality=fruit['quality']
        Name+=fruit['name'] + "\n"
print(Name)
#3 - Add 10 fruit to stock which fruti doesn't exist
for fruit in fruit_stock:
    if fruit['quality']==0:
        fruit['quality']=10
print(fruit_stock)
#4 - Add fruit name to array
array=[]
for fruit in fruit_stock:
    array.append(fruit['name'])
print(array)
#5 - Calculate total of price after add 10 to empty fruit
coum=0
for fruit in fruit_stock:
    if fruit['quality']==0:
        fruit['quality']=10
    sum+=fruit['quality']*fruit['price']
print(sum)