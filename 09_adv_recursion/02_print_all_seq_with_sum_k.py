nums = [17, 18, 6, 11, 2, 4] 
k = 6  
result = []

def all_seq(index, total, subset):
    if total == k:
        result.append(subset.copy())
        return
    elif total > k:
        return
    if index >= len(nums): 
        return
    subset.append(nums[index]) 
    all_seq(index+1, total + nums[index], subset)
    subset.pop() 
    all_seq(index+1, total, subset)

all_seq(0, 0, [])

print(result)