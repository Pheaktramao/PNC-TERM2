# Ex9 Array - Dictinary
arrText = ['banana','orange','coconut','mango']
arrNumber = [10, 30, 20, 9]
#Q - create array of dictionary following 2 array above
# [
#   {'banana':10},
#   {'orange': 30},
#   {'coconut': 20}
#   {'mango': 9}
# ]
newArr=[]
for i in range(len(arrText)):
    object={}
    object[arrText[i]]=arrNumber[i]
    newArr.append(object)
print(newArr)