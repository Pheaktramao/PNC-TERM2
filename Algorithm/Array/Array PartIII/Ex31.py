# Ex8 - Object
# #Reverse Object
input: {1: 'banana', 2: 'mango', 3: 'coconut'}
# output: {1: 'ananab', 2: 'ognam', 3: 'tunococ'}
def reverse(text):
    res=''
    for i in range(len(text)):
        res+=text[len(text)-(i+1)]
    return res

fruit={1: 'banana', 2: 'mango', 3: 'coconut'}
fg={}
for fri in fruit:
    fg[fri]=reverse(fruit[fri])
print(fg)