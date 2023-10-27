# 2.Count avoid Spaces in string length
# input:ab1 dc a
# output:6

def count(string):
    count=0
    for i in range(len(string)):
        if string[i]!=" ":
            count+=1
    return count
text=input()
print(count(text))