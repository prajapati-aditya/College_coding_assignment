nums = [1,2,1,2,1,2,3,1,3,2]
k = 2
# Output: [1,2]
freq = {}
for num in nums :
    if num in freq :
        freq[num] += 1
    else :
        freq[num] = 1
bucket = [[] for _ in range(len(nums) + 1)]
        
for num, count in freq.items():
    bucket[count].append(num)
    
print (bucket)

# traverse from back 
res = []
count = 0
for i in range(len(bucket)-1 , -1 ,-1) :
    for num in bucket[i] :
        res.append(num)
        count += 1
    if count == k :
        break
print(res)