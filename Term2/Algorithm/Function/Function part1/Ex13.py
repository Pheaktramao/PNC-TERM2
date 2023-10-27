def uppercase(string):
    result=""
    isspace=False
    for i in range(len(string)):
        if i==0:
            result+=string[i].upper()
        elif isspace:
            result+=string
print(uppercase(text))