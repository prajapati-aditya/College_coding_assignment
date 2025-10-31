nums = [1,7,3,6,5,6]

total = sum(nums)
left_sum = 0
for i , num in enumerate(nums) :
    if left_sum == total - (left_sum + num) :
        print(i)
        
    left_sum += num
     
    