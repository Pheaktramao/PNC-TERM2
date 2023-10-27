# Ex3 - Array append() function

array = []

#1 - add value from 1 to 10 in empty array
for i in range(1,11):
    array.append(i)
print(array)
#2 - add only even number to empty array from 1 to 20
for i in range(1,21):
    if i%2==0:
        array.append(i)
print(array)
#3 - add value to empty array from 10 to 1
for i in range (10):
    array.append(10-i)
print(array)
#4 - If input as a text example "hi" add each word to empty array => ["h","i"]
text=input()
for i in range(len(text)):
    array.append(text[i])
print(array)