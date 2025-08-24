nums = [1,99,101,98,2,5,3,4,100,100,102,103,1,1]

set_num = set([ele for ele in nums])

longest_count = 0
count = 0
for ele in set_num:
    is_start = ele-1 in set_num
    if is_start:
        pass
    else:
        while ele in set_num:
            count += 1
            ele += 1 
        longest_count = max(count, longest_count)
        count = 0
print(longest_count)