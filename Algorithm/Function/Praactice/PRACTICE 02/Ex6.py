def reverstring(string):
    result=""
    lastindex=len(string)-1
    for i in range(len(string)):
        result+=string[lastindex-i]
    return result
text=input()
print(reverstring(text))