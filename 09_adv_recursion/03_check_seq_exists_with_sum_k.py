nums = [17, 18, 6, 11, 2, 4] 
k = 1111 
result = []

def all_seq(index, total, subset):
    if total == k:
        result.append(subset.copy())
        return True
    elif total > k:
        return False
    if index >= len(nums): 
        return False
    subset.append(nums[index]) 
    pick = all_seq(index+1, total + nums[index], subset)
    if pick:
        return True
    subset.pop() 
    not_pick = all_seq(index+1, total, subset)
    return not_pick

print(all_seq(0,0,[]))