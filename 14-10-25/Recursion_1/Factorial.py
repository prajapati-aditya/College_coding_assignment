num = 5

def fact(num) :
    if num <=1 :
        return 1
    res = num*fact(num-1)
    return res

print(fact(num))