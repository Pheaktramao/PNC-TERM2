# 1.How to Remove number From a String in Python
# Input:yon12rady23him2
# output:yonradyhim
def getletter(string):
    result=""
    isNumber=False
    for i in range(len(string)):
        if string[i].isnumeric():
            isNumber=True
        else:
            result+=string[i]
    return result
text=input()
print(getletter(text))