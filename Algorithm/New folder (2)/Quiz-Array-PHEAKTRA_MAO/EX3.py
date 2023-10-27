def reverseString(word):
    result=""
    for i in range(len(word)):
        result+=word[-1-i]
    return result
text=input()
print(reverseString(text))
