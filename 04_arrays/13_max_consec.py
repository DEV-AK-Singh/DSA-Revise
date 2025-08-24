nums = [1,1,0,1,0,1,1,1,1,0,1,1,1,1,1]
largest_count = 0
curr_count = 0
for ele in nums:
    if ele == 0:
        curr_count = 0
    else:
        curr_count += 1
        largest_count = max(curr_count, largest_count)
print(largest_count)