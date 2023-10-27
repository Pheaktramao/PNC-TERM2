# def FindLetterA(word):
#     result=""
#     count=0
#     for i in range(len(word)):
#         if word[i]=="a":
#             count+=1 
#             result="Number of A is "+str(count)
#     return result
# array=input()
# print(FindLetterA(array))

def countLetterA(array):
    total=""
    count=0
    for i in range(len(array)):
        word=array[i]
        for j in range(len(word)):
            if word[j]=="a" or word[j]=="A":
                count+=1
        total+="Number of A in "+array[i]+" is "+str(count)+"\n"
    return total
array=eval(input())
print(countLetterA(array))