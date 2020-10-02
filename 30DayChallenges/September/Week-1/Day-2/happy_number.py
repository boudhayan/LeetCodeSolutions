
def isHappy(number):
    output = {}
    result = True
    while number != 1:
        if number in output:
            result = False
            break
        output[number] = True
        res = 0
        for ch in str(number):
            res = res + int(str(int(ch)**2))
        number = res
    return result

print(isHappy(66))