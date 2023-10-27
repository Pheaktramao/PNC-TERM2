def getAbsolute(number):
    if number < 0:
        return -1 * number
    else:
        return str(number)

print(getAbsolute(-5) + 10)
