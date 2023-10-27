def isEqual(list1,list2):
    i=0
    Equal=True
    while i<len(list1) and Equal:
        if list1[i]!=list2[i]:
            Equal=False
        i+=1
    return Equal        
list1=eval(input())
list2=eval(input())
if len(list1)==len(list2):
    isCorrect=isEqual(list1,list2)
    if not isCorrect:
        print("Not Equal")
    else:
        print("Equal")
else:
    print("Not Euqal")
