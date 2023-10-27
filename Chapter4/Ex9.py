# Ex8 - Dictinary
listFruit = [
  {'name': 'banan', 'price': 10, 'location': 'cambodia'},
  {'name': 'coconut', 'price': 30, 'location': 'Thailand'},
  {'name': 'Jackfruit', 'price': 90, 'location': 'India'},
  {'name': 'orange', 'price': 20, 'location': 'Singapore'},
  {'name': 'Orange', 'price': 8, 'location': 'USA'},
]
#1 - Find average of fruit price
sum=0
average=0
for fruit in listFruit:
    sum+=fruit['price']
average=sum/fruit['price']
print(average)
#2 - How many fruit type in list
fruitName=listFruit[0]['name']
count=0
for fruit in listFruit:
    if fruit['name']!=fruitName:
        count+=1
print(count)
# 3 - Which country has highest price of fruit
highprice=listFruit[0]['price']
Namefruit=""
for fruit in listFruit:
    if fruit['price']>=highprice:
        highprice=fruit['price']
        Namefruit=fruit['name']
print(Namefruit)
#4 - Which fruti has price lower than 30$
Namefruit=""
NewArr=[]
for fruit in listFruit:
    if fruit['price']<30:
        Namefruit=fruit['name']
        NewArr.append(Namefruit)
print(NewArr)
# ['banan','orange']
#5 - Which fruit name from Cambodia?
nameFruit=""
locate=listFruit[0]['location']
for fruit in listFruit:
    if fruit['location']=='cambodia':
        locate=fruit['location']
        nameFruit=fruit['name']
print(nameFruit)