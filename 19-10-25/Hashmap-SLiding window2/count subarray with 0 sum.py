arr = [0, 0, 5, 5, 0, 0]
store = {0:1}
count = 0
prSum = 0
for num in arr :
    prSum += num
    if prSum not in store :
           store[prSum] = 1
    else :
        count += store[prSum]
        store[prSum] = store[prSum]+1

print(count) 