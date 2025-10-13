from collections import Counter
nums = [1,1,2,2,3,4]
dict = Counter(nums)
res = 0
max_freq = 1
for num in dict.values() :
    if num > max_freq :
        max_freq = num
print(max_freq)
for key, value in dict.items() :
    if value == max_freq :
        res += value
print(res)