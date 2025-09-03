nums = [17, 18, 6, 11, 2, 4] 
k = 24

def all_seq(index, total):
    if total == k: 
        return 1
    elif total > k:
        return 0
    if index >= len(nums): 
        return 0 
    pick = all_seq(index+1, total + nums[index])   
    not_pick = all_seq(index+1, total)
    return pick + not_pick
 
print(all_seq(0,0))