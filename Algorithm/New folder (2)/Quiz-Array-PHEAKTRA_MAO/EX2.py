def ContainUpperCase(word):
    result=""
    isBig=False
    for i in range(len(word)):
        if word[i].isupper():
            isBig=True
    if isBig:
        result="VALID"
    else:
        result="INVALID"
    return result
text=input()
print(ContainUpperCase(text))