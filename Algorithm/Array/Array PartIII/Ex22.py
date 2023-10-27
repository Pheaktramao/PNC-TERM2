# Ex8 - Dictionary or object
fruit_stock = [
  {'id': 1, 'name': 'Coconut', 'quatity': 3, 'price': 4000},
  {'id': 2, 'name': 'Banana', 'quatity': 0, 'price': 2500},
  {'id': 3, 'name': 'Mango', 'quatity': 23, 'price': 2000},
  {'id': 4, 'name': 'Orange', 'quatity': 0, 'price': 5000},
  {'id': 5, 'name': 'Apple', 'quatity': 5, 'price': 3000},
  {'id': 6, 'name': 'Jackfruit', 'quatity': 13, 'price': 6000},
]
count=0
Name=[]
for fruit in fruit_stock:
    if fruit['price']>3000:
        count+=1
        Name.append(fruit['name'])
print("numberOffruit: "+str(count)+","+"\n" "names: "+str(Name))
# #1 - How many fruit have price > 3000

# {
#   'numberOfruit': 3,
#   'names': ['Coconut','Orange', 'Jackfruit']
# }
# --------------------
# #2 - How many fruit have price < 5000
# [
#   {'name': 'Coconut'},
#   {'name': 'Banana'},
#   {'name': 'Mango'},
#   {'name': 'Apple'}
# ]
# fruitName=""
Name=[]
for fruit in fruit_stock:
    if fruit['price']<5000:
        fruitName=fruit['name']
        name={}
        name['name']=fruitName
        Name.append(name)
print(Name)

# -------------------
# #3 - Which fruit doens't have in stock
# [
#   {'name': 'Banana', 'quatity': 0},
#   {'name': 'Orange', 'quatity': 0}
# ]
Array=[]
for fruit in fruit_stock:
    if fruit['quatity']==0:
        fruitName=fruit['name']
        quatity=fruit['quatity']
        object={}
        object['name']=fruitName
        object['quatity']=quatity
        Array.append(object)
print(Array)