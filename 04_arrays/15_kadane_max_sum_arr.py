nums = [-2,1-3,4,-1,2,1,-5,4,7]
max_sum = 0
curr_sum = 0
for ele in nums:
    curr_sum += ele
    max_sum = max(curr_sum, max_sum)
    if curr_sum < 0:
        curr_sum = 0
print(max_sum)