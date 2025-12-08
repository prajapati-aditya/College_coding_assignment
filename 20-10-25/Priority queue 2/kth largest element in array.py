import heapq
nums = [3,2,1,5,6,4]
k = 1
# Output: 5
nums= [-num for num in nums]
# create the heap
heapq.heapify(nums)
print(nums)
for _ in range(k-1) :
    heapq.heappop(nums)
    
print (-heapq.heappop(nums))