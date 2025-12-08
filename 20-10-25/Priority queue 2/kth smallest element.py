import heapq
nums = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k = 4
# Output: 5
heapq.heapify(nums)
print(nums)

for _ in range(k-1) :
    heapq.heappop(nums)
print(heapq.heappop(nums))
