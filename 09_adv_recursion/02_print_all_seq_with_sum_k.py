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
    sum = total + nums[index]
    all_seq(index+1, sum, subset)
    ele = subset.pop()
    sum = sum - ele
    all_seq(index+1, sum, subset)

all_seq(0, 0, [])

print(result)